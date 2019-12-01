from tkinter import *
from easygui import fileopenbox

name_of_user = "Semanur Gelturan \nHukuk"

BACKGROUND = "black"
FOREGROUND = "white"

def add_child_page(parent, *childs):
    for name, child in childs:
        child.parent_page = parent
        parent.child_pages[name] = child

class MainPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg = BACKGROUND)
        self.child_pages = dict()
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        self.pack(fill = BOTH, expand = True)

        top_frame = Frame(self, bg = BACKGROUND)
        profile_photo = Button(top_frame, text = "[]", width = 10, height = 3, bg = BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable = self.user_name_var, bg = BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text = "?")
        notification_button = Button(top_frame, text = chr(7))

        top_frame.pack(fill = X, side = TOP)
        profile_photo.pack(side = LEFT)
        user_name.pack(side = LEFT)
        notification_button.pack(side = RIGHT)
        help_button.pack(side = RIGHT)


        page_button_frame = Frame(self, bg = BACKGROUND)
        profile_button = Button(page_button_frame, text = "Profil bilgileri", font = "Area 12 bold", borderwidth = 0, bg = BACKGROUND, fg = FOREGROUND, command = lambda:self.go_to_page(self.child_pages["profile"]))
        society_button = Button(page_button_frame, text = "Society'ler", font = "Area 12 bold", borderwidth = 0, bg = BACKGROUND, fg = FOREGROUND, command = lambda:self.go_to_page(self.child_pages["society"]))
        club_button = Button(page_button_frame, text = "Kulüp", font = "Area 12 bold", borderwidth = 0, bg = BACKGROUND, fg = FOREGROUND, command = lambda:self.go_to_page(self.child_pages["club"]))

        page_button_frame.pack(fill = Y, expand = True)
        profile_button.pack(fill = BOTH, expand = True)
        society_button.pack(fill = BOTH, expand = True)
        club_button.pack(fill = BOTH, expand = True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill = BOTH, expand = True)


class ProfilePage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg = BACKGROUND)
        back_button = Button(top_frame, text = "<", bg = BACKGROUND, fg = FOREGROUND, command = self.go_back)
        profile_photo = Button(top_frame, text = "[]", width = 10, height = 3, bg = BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable = self.user_name_var, bg = BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text = "?")
        notification_button = Button(top_frame, text = chr(7))

        top_frame.pack(fill = X, side = TOP)
        back_button.pack(side = LEFT)
        profile_photo.pack(side = LEFT)
        user_name.pack(side = LEFT)
        notification_button.pack(side = RIGHT)
        help_button.pack(side = RIGHT)


        page_button_frame = Frame(self, bg = BACKGROUND)
        attended_events = Button(page_button_frame, text = "Katıldığım Etkinlikler", font = "Area 12 bold", borderwidth = 0, bg = BACKGROUND, fg = FOREGROUND, command = lambda:self.go_to_page(self.child_pages["attended events"]))
        events_i_can_attend = Button(page_button_frame, text = "Katılabileceğim Etkinlikler", font = "Area 12 bold", borderwidth = 0, bg = BACKGROUND, fg = FOREGROUND, command = lambda:self.go_to_page(self.child_pages["events i can attend"]))
        add_friend = Button(page_button_frame, text = "Arkadaş Ekle", font = "Area 12 bold", borderwidth = 0, bg = BACKGROUND, fg = FOREGROUND, command = lambda:self.go_to_page(self.child_pages["add friend"]))
        account_information = Button(page_button_frame, text = "Hesap Bilgileri", font = "Area 12 bold", borderwidth = 0, bg = BACKGROUND, fg = FOREGROUND, command = lambda:self.go_to_page(self.child_pages["account information"]))


        page_button_frame.pack(fill = BOTH, expand = True)
        attended_events.pack(fill = BOTH, expand = True)
        events_i_can_attend.pack(fill = BOTH, expand = True)
        add_friend.pack(fill = BOTH, expand = True)
        account_information.pack(fill = BOTH, expand = True)


    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill = BOTH, expand = True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill = BOTH, expand = True)


class SocietyPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg = BACKGROUND)
        back_button = Button(top_frame, text = "<", bg = BACKGROUND, fg = FOREGROUND, command = self.go_back)
        profile_photo = Button(top_frame, text = "[]", width = 10, height = 3, bg = BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable = self.user_name_var, bg = BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text = "?")
        notification_button = Button(top_frame, text = chr(7))

        top_frame.pack(fill = X, side = TOP)
        back_button.pack(side = LEFT)
        profile_photo.pack(side = LEFT)
        user_name.pack(side = LEFT)
        notification_button.pack(side = RIGHT)
        help_button.pack(side = RIGHT)


        page_button_frame = Frame(self, bg = BACKGROUND)
        cs = Button(page_button_frame, text = "CS", font = "Area 12 bold", borderwidth = 0, bg = BACKGROUND, fg = FOREGROUND, command = lambda:self.go_to_page(self.child_pages["cs"]))
        wie = Button(page_button_frame, text = "WIE", font = "Area 12 bold", borderwidth = 0, bg = BACKGROUND, fg = FOREGROUND, command = lambda:self.go_to_page(self.child_pages["wie"]))
        ea = Button(page_button_frame, text = "EA", font = "Area 12 bold", borderwidth = 0, bg = BACKGROUND, fg = FOREGROUND, command = lambda:self.go_to_page(self.child_pages["ea"]))
        ras = Button(page_button_frame, text = "RAS", font = "Area 12 bold", borderwidth = 0, bg = BACKGROUND, fg = FOREGROUND, command = lambda:self.go_to_page(self.child_pages["ras"]))
        pes = Button(page_button_frame, text = "PES", font = "Area 12 bold", borderwidth = 0, bg = BACKGROUND, fg = FOREGROUND, command = lambda:self.go_to_page(self.child_pages["pes"]))


        page_button_frame.pack(fill = BOTH, expand = True)
        cs.pack(fill = BOTH, expand = True)
        wie.pack(fill = BOTH, expand = True)
        ea.pack(fill = BOTH, expand = True)
        ras.pack(fill = BOTH, expand = True)
        pes.pack(fill = BOTH, expand = True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)


class ClubPage(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg = BACKGROUND)
        back_button = Button(top_frame, text = "<", bg = BACKGROUND, fg = FOREGROUND, command = self.go_back)
        profile_photo = Button(top_frame, text = "[]", width = 10, height = 3, bg = BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable = self.user_name_var, bg = BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text = "?")
        notification_button = Button(top_frame, text = chr(7))

        top_frame.pack(fill = X, side = TOP)
        back_button.pack(side = LEFT)
        profile_photo.pack(side = LEFT)
        user_name.pack(side = LEFT)
        notification_button.pack(side = RIGHT)
        help_button.pack(side = RIGHT)


        page_button_frame = Frame(self, bg = BACKGROUND)
        yk = Button(page_button_frame, text = "YK", font = "Area 12 bold", borderwidth = 0, bg = BACKGROUND, fg = FOREGROUND, command = lambda:self.go_to_page(self.child_pages["yk"]))
        purpose = Button(page_button_frame, text = "Tanıtımı / Amacı", font = "Area 12 bold", borderwidth = 0, bg = BACKGROUND, fg = FOREGROUND, command = lambda:self.go_to_page(self.child_pages["purpose"]))


        page_button_frame.pack(fill = BOTH, expand = True)
        yk.pack(fill = BOTH, expand = True)
        purpose.pack(fill = BOTH, expand = True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)


class EventsICanAttend(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        comment = Button(page_button_frame, text="Daha Önceki Yorumlara Göre", font="Area 12 bold", borderwidth=0, bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["review"]))
        society = Button(page_button_frame, text="Society'nin Başarısına Göre", font="Area 12 bold", borderwidth=0, bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["society"]))
        interest = Button(page_button_frame, text="Etkinliğe Gösterilen İlgiye Göre", font="Area 12 bold", borderwidth=0, bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["interest"]))
        friends = Button(page_button_frame, text="Arkadaşlarınızın Seçimlerine Göre", font="Area 12 bold", borderwidth=0, bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["friends"]))
        time = Button(page_button_frame, text="Zamana Göre", font="Area 12 bold", borderwidth=0, bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["time"]))

        page_button_frame.pack(fill=BOTH, expand=True)
        comment.pack(fill=BOTH, expand=True)
        society.pack(fill=BOTH, expand=True)
        interest.pack(fill=BOTH, expand=True)
        friends.pack(fill=BOTH, expand=True)
        time.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)

class AccountInformation(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        edit_profile = Button(page_button_frame, text="Profili Düzenle", font="Area 12 bold", borderwidth=0, bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["edit profile"]))
        change_password = Button(page_button_frame, text="Şifreyi Değiştir", font="Area 12 bold", borderwidth=0, bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["change password"]))
        log_out = Button(page_button_frame, text="Çıkış Yap", font="Area 12 bold", borderwidth=0, bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["log out"]))
        delete_account = Button(page_button_frame, text="Hesabı Sil", font="Area 12 bold", borderwidth=0, bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["delete account"]))

        page_button_frame.pack(fill=BOTH, expand=True)
        edit_profile.pack(fill=BOTH, expand=True)
        change_password.pack(fill=BOTH, expand=True)
        log_out.pack(fill=BOTH, expand=True)
        delete_account.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)

class AttendedEvents(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        # attended_events = Button(page_button_frame, text="Katıldığım Etkinlikler", font="Area 12 bold", borderwidth=0, bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["attended events"]))

        page_button_frame.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)


class AddFriend(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        # attended_events = Button(page_button_frame, text="Katıldığım Etkinlikler", font="Area 12 bold", borderwidth=0, bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["attended events"]))

        page_button_frame.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)


class BasedOnReviews(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.top_variables = {0: StringVar(), 1: StringVar(), 2: StringVar()}
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        top1 = Label(page_button_frame, textvariable = self.top_variables[0], font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND)
        top2 = Label(page_button_frame, textvariable = self.top_variables[1], font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND)
        top3 = Label(page_button_frame, textvariable = self.top_variables[2], font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND)

        page_button_frame.pack(fill=BOTH, expand=True)
        top1.pack(fill=BOTH, expand=True)
        top2.pack(fill=BOTH, expand=True)
        top3.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)



class BasedOnSocietySuccess(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        # attended_events = Button(page_button_frame, text="Katıldığım Etkinlikler", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["attended events"]))

        page_button_frame.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)



class BasedOnOInterest(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        # attended_events = Button(page_button_frame, text="Katıldığım Etkinlikler", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["attended events"]))

        page_button_frame.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)



class BasedOnChooseOfFriends(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        # attended_events = Button(page_button_frame, text="Katıldığım Etkinlikler", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["attended events"]))

        page_button_frame.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)



class BasedOnTime(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        # attended_events = Button(page_button_frame, text="Katıldığım Etkinlikler", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["attended events"]))

        page_button_frame.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)



class EditProfile(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        photo = Button(page_button_frame, text="[]", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND)
        change_photo = Button(page_button_frame, text="Fotoğrafı Değiştir", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command = fileopenbox)

        page_button_frame.pack(fill=BOTH, expand=True)
        photo.pack(fill=BOTH, expand=True)
        change_photo.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)



class ChangePassword(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.old_password = StringVar()
        self.old_password.set("Eski Şifre:")
        self.new_password = StringVar()
        self.new_password.set("Yeni Şifre:")
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        old_password = Entry(page_button_frame, textvariable = self.old_password)
        new_password = Entry(page_button_frame, textvariable = self.new_password)
        change = Button(page_button_frame, text="Şifreyi Değiştir", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND)

        page_button_frame.pack(fill=BOTH, expand=True)
        old_password.pack(fill=BOTH, expand=True, padx = 100, pady = (50,50))
        new_password.pack(fill=BOTH, expand=True, padx = 100, pady = (0,50))
        change.pack(fill=BOTH, expand=True, pady = (0,50))

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)



class LogOut(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        question = Label(page_button_frame, text="Çıkış yapmak İstediğinden Emin Misin?", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND)
        yes = Button(page_button_frame, text="Evet", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=exit)
        no = Button(page_button_frame, text="Hayır", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)

        page_button_frame.pack(fill=BOTH, expand=True)
        question.pack(fill=BOTH, expand=True)
        yes.pack(fill=BOTH, expand=True)
        no.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)



class DeleteAccount(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        question = Button(page_button_frame, text="7 Gün İçinde Giriş Yapmazsanız Hesabınız Kaldırılacak.\nOnaylıyor musunuz?", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND)
        yes = Button(page_button_frame, text="Evet", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command = exit)
        no = Button(page_button_frame, text="Hayır", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command = self.go_back)

        page_button_frame.pack(fill=BOTH, expand=True)
        question.pack(fill=BOTH, expand=True)
        yes.pack(fill=BOTH, expand=True)
        no.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)



class Society(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        success = Button(page_button_frame, text="Society'nin Başarısı", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["success"]))
        purpose = Button(page_button_frame, text="Society'nin Amacı / Tanıtımı", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["purpose"]))
        members = Button(page_button_frame, text="Society'nin Ekibi", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["members"]))

        page_button_frame.pack(fill=BOTH, expand=True)
        success.pack(fill=BOTH, expand=True)
        purpose.pack(fill=BOTH, expand=True)
        members.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)

class SuccessOfSociety(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        activity = Button(page_button_frame, text="Aktifliğe Göre", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["activity"]))
        invited = Button(page_button_frame, text="Davetliye Göre", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["invited"]))
        leader = Button(page_button_frame, text="Yöneticiye Göre", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["leader"]))

        page_button_frame.pack(fill=BOTH, expand=True)
        activity.pack(fill=BOTH, expand=True)
        invited.pack(fill=BOTH, expand=True)
        leader.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)


class PurposeOfSociety(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        # attended_events = Button(page_button_frame, text="Katıldığım Etkinlikler", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["attended events"]))

        page_button_frame.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)


class MemberOfSociety(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        # attended_events = Button(page_button_frame, text="Katıldığım Etkinlikler", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["attended events"]))

        page_button_frame.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)


class Activity(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        # attended_events = Button(page_button_frame, text="Katıldığım Etkinlikler", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["attended events"]))

        page_button_frame.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)


class Invited(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        # attended_events = Button(page_button_frame, text="Katıldığım Etkinlikler", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["attended events"]))

        page_button_frame.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)


class Leader(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        # attended_events = Button(page_button_frame, text="Katıldığım Etkinlikler", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["attended events"]))

        page_button_frame.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)


class Yk(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        # attended_events = Button(page_button_frame, text="Katıldığım Etkinlikler", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["attended events"]))

        page_button_frame.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)


class Purpose(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.child_pages = dict()
        self.parent_page = None
        self.user_name_var = StringVar()
        self.user_name_var.set(name_of_user)
        self.init_UI()

    def init_UI(self):
        top_frame = Frame(self, bg=BACKGROUND)
        back_button = Button(top_frame, text="<", bg=BACKGROUND, fg = FOREGROUND, command=self.go_back)
        profile_photo = Button(top_frame, text="[]", width=10, height=3, bg=BACKGROUND, fg = FOREGROUND)
        user_name = Label(top_frame, textvariable=self.user_name_var, bg=BACKGROUND, fg = FOREGROUND)
        help_button = Button(top_frame, text="?")
        notification_button = Button(top_frame, text=chr(7))

        top_frame.pack(fill=X, side=TOP)
        back_button.pack(side=LEFT)
        profile_photo.pack(side=LEFT)
        user_name.pack(side=LEFT)
        notification_button.pack(side=RIGHT)
        help_button.pack(side=RIGHT)

        page_button_frame = Frame(self, bg=BACKGROUND)
        # attended_events = Button(page_button_frame, text="Katıldığım Etkinlikler", font="Area 12 bold", borderwidth=0,  bg=BACKGROUND, fg = FOREGROUND, command=lambda: self.go_to_page(self.child_pages["attended events"]))

        page_button_frame.pack(fill=BOTH, expand=True)

    def go_to_page(self, page):
        self.pack_forget()
        page.pack(fill=BOTH, expand=True)

    def go_back(self):
        self.pack_forget()
        self.parent_page.pack(fill=BOTH, expand=True)

