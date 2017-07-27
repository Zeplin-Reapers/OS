import time
import tkinter as tk
import os
import random
import math
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

        self.b4 = tk.Button(self, bg="blue")
        self.b4["text"] = "delete file infromation"
        self.b4["command"] = self.number5
        self.b4.pack(side="left")

        self.b5 = tk.Button(self, bg="silver")
        self.b5["text"] = "Games"
        self.b5["command"] = self.number4
        self.b5.pack(side="left")

        self.b6 = tk.Button(self, bg="teal")
        self.b6["text"] = "Calculator"
        self.b6["command"] = self.number6
        self.b6.pack(side="left")

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
    def number4(self):
        print("Games: pick a number")
        game = input("Pick a game: ")
        if "number" in game:
            num = random.randint(1,100)
            print(num)
            guess = input("Pick a number 1 to 100: ")
            while int(guess) != num:
               guess = input("guess again: ")
            print("Congrats! You Won!")
    def number5(self):
        file00 = open("file/file.txt", "w")
        file00.write("")
    def number6(self):
        n1 = int(input("first number: "))
        n2 = int(input("second number: "))
        print("The options for the operater are:")
        print(" power")
        print(" square root")
        op = input("operator: ")
        if "power" in  op:
            print(math.pow(n1,n2))
        elif "square root" in op:
            print(math.sqrt(n1))
root = tk.Tk()
app = Application(master=root)
app.mainloop()
