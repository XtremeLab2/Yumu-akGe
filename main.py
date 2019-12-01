from NLP import *
from GUI import *


database = DataBase()
most_top = list()
for event in database.for_test:
    most_top.append((database.recommend(event.content, STUDENT_NUMBER), event.event_name))
most_top.sort()
most_top.reverse()
most_top = most_top[:3]


root = Tk()
root.title("deneme")
root.geometry("500x400+200+200")
main_page = MainPage(root)

profile_page = ProfilePage(root)
society_page = SocietyPage(root)
club_page = ClubPage(root)

add_child_page(main_page, ("profile", profile_page), ("society", society_page), ("club", club_page))

attended_events = AttendedEvents(root)
events_i_can_attend = EventsICanAttend(root)
add_friend = AddFriend(root)
account_information = AccountInformation(root)

add_child_page(profile_page, ("attended events", attended_events), ("events i can attend", events_i_can_attend), ("add friend", add_friend), ("account information", account_information))

based_on_reviews = BasedOnReviews(root)
based_on_society = BasedOnSocietySuccess(root)
based_on_interest = BasedOnOInterest(root)
based_on_friends = BasedOnChooseOfFriends(root)
based_on_time = BasedOnTime(root)

add_child_page(events_i_can_attend, ("review", based_on_reviews),  ("society", based_on_society),  ("interest", based_on_interest),  ("friends", based_on_friends),  ("time", based_on_time))

edit_profile = EditProfile(root)
change_password = ChangePassword(root)
log_out = LogOut(root)
delete_account = DeleteAccount(root)

add_child_page(account_information, ("edit profile", edit_profile), ("change password", change_password), ("log out", log_out), ("delete account", delete_account))

cs = Society(root)
wie = Society(root)
ea = Society(root)
ras = Society(root)
pes = Society(root)

add_child_page(society_page, ("cs", cs), ("wie", wie), ("ea", ea), ("ras", ras), ("pes", pes))

success_of_society = SuccessOfSociety(root)
purpose_of_society = PurposeOfSociety(root)
members_of_society = MemberOfSociety(root)

for society in [cs, wie, ea, ras, pes]:
    add_child_page(society, ("success", success_of_society), ("purpose", purpose_of_society), ("members", members_of_society))

activity = Activity(root)
invited = Invited(root)
leader = Leader(root)

add_child_page(success_of_society, ("activity", activity), ("invited", invited), ("leader", leader))

yk = Yk(root)
purpose = Purpose(root)

add_child_page(club_page, ("yk", yk), ("purpose", purpose))

for index in range(len(most_top)):
    based_on_reviews.top_variables[index].set(most_top[index][1])

root.mainloop()