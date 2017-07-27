import time
import tkinter as tk
version = "alpha 0"
full = "false"
print("OS VERSION: " + version + ";")
print("FULL REALESE: " + full + ";")
print("Loading")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
print("complete!")
time.sleep(0.5)
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

