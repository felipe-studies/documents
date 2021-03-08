import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

class WindowOne(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="User Registration")
        self.set_size_request(360, 240)
        self.set_border_width(16)
        self.timeout_id = None

        self.update_user = True  # if PUT method, update user at DB
        self.user_name = ""  # complete name of user
        self.user_id = 0  # user database ID 

        self.name_entry_text = False
        self.lastname_entry_text = False
        self.progress_bar_percent = 0

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=24)
        self.add(box)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)

        if self.update_user:
            box_title = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)

            self.label_title = Gtk.Label()
            label_text = "Updating User " + str(self.user_name) + " (ID: " + str(self.user_id) + ")"
            self.label_title.set_text(label_text)
            self.label_title.set_justify(Gtk.Justification.LEFT)

            box.pack_start(box_title, False, True, 0)
            box_title.pack_start(self.label_title, False, False, 0)

        box.pack_start(vbox, False, True, 0)
        box.pack_end(hbox, False, True, 0)
        hbox.pack_start(hbox2, True, True, 0)

        self.label_name = Gtk.Label()
        self.label_name.set_text("First Name:")
        self.label_name.set_justify(Gtk.Justification.LEFT)
        vbox.add(self.label_name)

        self.entry_name = Gtk.Entry()
        self.entry_name.set_max_length(50)
        self.entry_name.set_text("")
        self.entry_name.connect("changed", self.on_entry_name_changed)
        vbox.add(self.entry_name)

        self.label_lastname = Gtk.Label()
        self.label_lastname.set_text("Last Name:")
        self.label_lastname.set_justify(Gtk.Justification.LEFT)
        vbox.add(self.label_lastname)

        self.entry_lastname = Gtk.Entry()
        self.entry_lastname.set_max_length(50)
        self.entry_lastname.set_text("")
        self.entry_lastname.connect("changed", self.on_entry_lastname_changed)
        vbox.add(self.entry_lastname)

        self.progressbar = Gtk.ProgressBar()
        self.progressbar.set_text("Register Progress Completed: 0.0%")
        self.progressbar.set_show_text(True)
        vbox.add(self.progressbar)

        self.button_close = Gtk.Button(label="Cancel")
        self.button_close.connect("clicked", self.on_close_clicked)
        hbox2.pack_start(self.button_close, False, False, 0)

        self.dialog = Gtk.Button(label="Confirm")
        self.dialog.connect("clicked", self.on_question_clicked)
        hbox2.pack_end(self.dialog, False, False, 0)

        self.button = Gtk.Button.new_with_label("Update")
        self.button.connect("clicked", self.on_click_me_clicked)
        hbox2.pack_end(self.button, False, False, 0)

    def update_progressbar_percent(self):
        self.progressbar.set_fraction(self.progress_bar_percent)
        self.progressbar.set_text("Register Progress Completed: " + str(self.progress_bar_percent * 100) + "%")

    def on_entry_name_changed(self, entry):
        if len(entry.get_text()) >= 1 and not self.name_entry_text:
            self.name_entry_text = True
            self.progress_bar_percent += 0.5
            self.update_progressbar_percent()
        elif len(entry.get_text()) < 1:
            self.name_entry_text = False
            self.progress_bar_percent -= 0.5
            self.update_progressbar_percent()

    def on_entry_lastname_changed(self, entry):
        if len(entry.get_text()) >= 1 and not self.lastname_entry_text:
            self.lastname_entry_text = True
            self.progress_bar_percent += 0.5
            self.update_progressbar_percent()
        elif len(entry.get_text()) < 1:
            self.lastname_entry_text = False
            self.progress_bar_percent -= 0.5
            self.update_progressbar_percent()

    def on_close_clicked(self, button):
        print("Application Closed")
        Gtk.main_quit()

    def on_click_me_clicked(self, button):
        print('Clicked Update button')

    def on_question_clicked(self, widget):
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.QUESTION,
            buttons=Gtk.ButtonsType.YES_NO,
            text="Confirmation of Data Inserted",
        )
        dialog.format_secondary_text(
            "Are you sure of the data inserted?\nUsers created can be deleted later."
        )
        response = dialog.run()
        if response == Gtk.ResponseType.YES:
            print("clicked YES button")
        elif response == Gtk.ResponseType.NO:
            print("clicked NO button")

        dialog.destroy()


win = WindowOne()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()