import tkinter as tk
import time
import os
import sys
import math
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.b1 = tk.Button(self, bg="gold")
        self.b1["text"] = "Main apps"
        self.b1["command"] = self.b1i
        self.b1.pack(side="left")

        self.quit = tk.Button(self, text="QUIT", bg="red",
                              command=root.destroy)
        self.quit.pack(side="right")
    
    def b1i(self):
        with open("main apps.py") as f:
            code = compile(f.read(), "somefile.py", 'exec')
            exec(code)

root = tk.Tk()
root.title("BOOT")
app = Application(master=root)
app.mainloop()
