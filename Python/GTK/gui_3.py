import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

class WindowOne(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Example 3")
        self.set_size_request(480, 360)
        self.set_border_width(16)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.timeout_id = None

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.add(box)
        box_innermain = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=24)
        box_input1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        box_input_text1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        box_input2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        box_input_text2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)

        box.pack_start(box_innermain, False, False, 0)
        box_innermain.pack_start(box_input1, False, False, 0)
        box_innermain.pack_start(box_input2, False, False, 0)
        box_input1.pack_start(box_input_text1, True, True, 0)
        box_input2.pack_start(box_input_text2, True, True, 0)

        box.pack_end(hbox, False, True, 0)
        hbox.pack_start(hbox2, True, True, 0)

        self.label_username = Gtk.Label()
        self.label_username.set_text("Username:")
        self.label_username.set_justify(Gtk.Justification.LEFT)
        box_input_text1.pack_start(self.label_username, False, False, 0)

        self.entry_username = Gtk.Entry()
        self.entry_username.set_max_length(50)
        self.entry_username.set_text("")
        box_input1.pack_start(self.entry_username, False, False, 0)

        self.label_password = Gtk.Label()
        self.label_password.set_text("Password:")
        self.label_password.set_justify(Gtk.Justification.LEFT)
        box_input_text2.pack_start(self.label_password, False, False, 0)

        self.entry_password = Gtk.Entry()
        self.entry_password.set_visibility(False)
        self.entry_password.set_max_length(50)
        self.entry_password.set_text("")
        box_input2.pack_start(self.entry_password, False, False, 0)

        self.button_close = Gtk.Button(label="Cancel")
        self.button_close.connect("clicked", self.on_close_clicked)
        hbox2.pack_start(self.button_close, False, False, 0)

        self.button = Gtk.Button.new_with_label("Confirm")
        self.button.connect("clicked", self.on_click_me_clicked)
        hbox2.pack_end(self.button, False, False, 0)

    def on_close_clicked(self, button):
        print("Application Closed")
        Gtk.main_quit()

    def on_click_me_clicked(self, button):
        print('Clicked Update button')

win = WindowOne()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()