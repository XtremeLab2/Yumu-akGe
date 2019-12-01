from os.path import join, basename
from os import getcwd, listdir
from bs4 import BeautifulSoup
import requests
from docclass import getwords, naivebayes
import xlrd

STUDENT_NUMBER = "217471064"

class User:

    def __init__(self, student_number):
        self.student_number = student_number
        self.rates_for_societies = dict() # { society_tag: rate }
        self.attended_events = dict() # [ event_name: rate, event_name: rate, ... ]

    def add_event(self, event_object, rate):
        self.attended_events[event_object] = rate

class Society:

    def __init__(self, tag):
        self.tag = str()
        self.event_list = list() # [ event1, event2... ]

    def add_event(self, event_object):
        self.event_list.append(event_object)

class Event:

    def __init__(self, event_name, society_name, content):
        self.event_name = event_name
        self.society_name = society_name
        self.content = content
        self.user_rates = dict() # { student_number: rate }

    def add_user_rate(self, student_number, rate):
        self.user_rates[student_number] = rate

class DataBase:

    def __init__(self):
        self.critics = dict() #{ user_object: {society: rate} }
        self.user_dict = dict() # { student_number: user object }
        self.society_dict = dict() # { tag: society object }
        self.for_train = list()
        self.for_test = list()
        self.classifier = naivebayes(getwords)
        self.import_data(self.fetch_from("https://site.ieee.org/sb-sehir/xtremelab-2/", "comments"))
        for society in self.society_dict.values():
            for event in society.event_list:
                if event in self.for_train:
                    self.classifier.train(event.content, event.society_name)


    def import_data(self, event_list):
        for event in event_list:
            if not event.user_rates:
                self.for_test.append(event)
            else:
                self.for_train.append(event)
            if not event.society_name in self.society_dict:
                self.society_dict[event.society_name] = Society(event.society_name)

            self.society_dict[event.society_name].add_event(event)
            for student_number, rate in event.user_rates.items():
                if not student_number in self.user_dict:
                    self.user_dict[student_number] = User(student_number)
                self.user_dict[student_number].add_event(self.society_dict[event.society_name].event_list[-1], rate)

        default_rates = self.society_dict.copy()
        for tag in default_rates:
            default_rates[tag] = 2.5

        for student_number in self.user_dict:
            self.user_dict[student_number].rates_for_societies = default_rates.copy()

        self.calcutate_rates()
        for user in self.user_dict.values():
            self.critics[user.student_number] = user.rates_for_societies

    def calcutate_rates(self):
        for user in self.user_dict.values():
            for society in self.society_dict.values():
                attended_events_for_current_society = 0
                total_points_for_current_society = 0
                for event in user.attended_events:
                    if event in society.event_list:
                        attended_events_for_current_society += 1
                        total_points_for_current_society += user.attended_events[event]
                if attended_events_for_current_society:
                    user.rates_for_societies[society.tag] = total_points_for_current_society / attended_events_for_current_society
                else:
                    user.rates_for_societies[society.tag] = 2.5

    def fetch_from(self, web_address, sub_directory):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        event_name = list()
        event_contents = list()
        event_list = list()
        events = BeautifulSoup(requests.get(web_address, headers = headers).text, features="html.parser").find(class_ = "entry-content")
        for event in events.find_all(class_ = "wpb_text_column wpb_content_element"):
            for tag in event.find_all("p"):
                if tag.find_all("strong", text = "Etkinlik Açıklaması:"):
                    content = tag.text[len("Etkinlik Açıklaması:")+1:]

                if tag.find_all("strong", text="Society:"):
                    society_name = tag.text[len("Society:") + 1:]
            event_contents.append((society_name, content))

        for event in events.find_all("h2"):
            event_name.append(event.text)

        for index in range(len(event_name)):
            event_list.append(Event(event_name[index], event_contents[index][0], event_contents[index][1]))

        header_index = 1
        comment_index = 7
        rates = dict()
        data_path = join(getcwd(), sub_directory)
        for file_number in range(len(listdir(data_path))):
            file_name = listdir(data_path)[file_number][:-5]
            excel_path = join(data_path, listdir(data_path)[file_number])
            sheet = xlrd.open_workbook(excel_path).sheets()[0]
            for index in range(len(sheet.col_values(header_index)[1:])):
                if sheet.col_values(header_index)[1:][index]:
                    if file_name not in rates:
                        rates[file_name] = dict()
                    rates[file_name][str(int(sheet.col_values(header_index)[1:][index]))] = self.predict_point(sheet.col_values(comment_index)[1:][index])


        for event in event_list:
            if event.event_name in rates:
                for event_name in rates:
                    if event_name == event.event_name:
                        event.user_rates = rates[event_name]
        return event_list

    def recommend(self, content, student_number):
        match_rates = self.classify(self.classifier, content)

        total = 0
        for rate, society_name in match_rates:
            total += rate * self.user_dict[student_number].rates_for_societies[society_name]
        return total


    def classify(self, classifier, content):
        match_rates = list()
        for society_name in classifier.categories():
            match_rates.append((classifier.prob(content, society_name), society_name))
        return match_rates

    def predict_point(self, comment):
        good_words = ["başarı", "iyi", "faydalı", "yardımcı", "güzel", "çekici", "teşekkür", "fırsat", "avantaj"]
        bad_words = ["rezalet", "kötü", "harca", "çirkin", "itici", "dezavantaj"]
        double_words = ["çok"]
        reverse_words = ["değil", "ama"]
        multipliers = list()
        good = 0
        bad = 0
        if bad + good == 0:
            return 2.5
        for word in good_words:
            if word in comment:
                good += 1
        for word in bad_words:
            if word in comment:
                bad += 1
        for word in double_words:
            if word in comment:
                multipliers.append(2)
                break
        for word in reverse_words:
            if word in comment:
                multipliers.append(-1)
                break
        for multiplier in multipliers:
            good *= multiplier
        return good / (good + bad)

