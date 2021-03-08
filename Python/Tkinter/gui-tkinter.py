import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Display Hello World"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.color_button = False
        self.fred = tk.Button(self, fg="red")
        self.fred["text"] = "Button test"
        self.fred["command"] = self.change_color
        self.fred["fg"] = "red"
        self.fred.config(fg="red")
        self.fred.pack()  # defaults to side = "top"
        self.fred.pack(side="left")
        self.fred.pack(expand=1)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def change_color(self):
        if not self.color_button:
            self.fred["fg"] = "blue"
            self.fred.config(fg="blue")
            self.color_button = True
        else:
            self.fred["fg"] = "red"
            self.fred.config(fg="red")
            self.color_button = False

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()