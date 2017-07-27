import time
import tkinter as tk
import sys
version = "alpha 1.0"
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
count = 1
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.b1 = tk.Button(self, bg="gold")
        self.b1["text"] = "Welcome"
        self.b1["command"] = self.number
        self.b1.pack(side="left")

        self.b2 = tk.Button(self, bg="blue")
        self.b2["text"] = "read file"
        self.b2["command"] = self.number2
        self.b2.pack(side="left")

        self.b3 = tk.Button(self, bg="blue")
        self.b3["text"] = "write to a file"
        self.b3["command"] = self.number3
        self.b3.pack(side="left")

        self.quit = tk.Button(self, text="QUIT", bg="red",
                              command=root.destroy)
        self.quit.pack(side="right")
    
    def number(self):
        print("Welcome to the Crystalyte OS!")
        time.sleep(0.5)
        print("here you have a small OS that is hosted on github.")
        time.sleep(0.5)
        print("https://www.github.com/zeplin-reapers/OS")
        print("\n" * 5)
    def number2(self):
        file = open("file/file.txt", "r")
        print(file.read())
    def number3(self):
        val = input("Your Text: ")
        file = open("file/file.txt", "a")
        file.write(val)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
