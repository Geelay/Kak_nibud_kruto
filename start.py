import math
import time 
import random
from tkinter import *
def start():
    root = Tk()
    frame = Frame(root)
    root.overrideredirect(True)
    root.overrideredirect(False)
    root.attributes('-fullscreen', True)
    canva = Canvas(root, bg='white')
    canva.pack(fill=BOTH, expand=1)
    photo = PhotoImage(file="pushkagame.png")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    Label(root, image=photo).place(x=screen_width/2, y=screen_height/2, anchor="center")
    btn = Button(root, text="Start game", width=30, height=5, bg="#FF5733", fg="black")

    def deletescreen(event):
        root.destroy()

    btn.bind("<Button-1>", deletescreen)
    btn.pack()
    root.mainloop()
def finish1():
    root = Tk()
    frame = Frame(root)
    root.overrideredirect(True)
    root.overrideredirect(False)
    root.attributes('-fullscreen', True)
    canva = Canvas(root, bg='black')
    canva.pack(fill=BOTH, expand=1)
    photo = PhotoImage(file="win.png")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    Label(root, image=photo).place(x=screen_width/2, y=screen_height/2, anchor="center")
    btn = Button(root, text="Pleasantly!", width=30, height=5, bg="#FF5733", fg="black")

    def deletescreen(event):
        root.destroy()

    btn.bind("<Button-1>", deletescreen)
    btn.pack()
    root.mainloop()
def finish2():
    root = Tk()
    frame = Frame(root)
    root.overrideredirect(True)
    root.overrideredirect(False)
    root.attributes('-fullscreen', True)
    canva = Canvas(root, bg='black')
    canva.pack(fill=BOTH, expand=1)
    photo = PhotoImage(file="lose.png")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    Label(root, image=photo).place(x=screen_width/2, y=screen_height/2, anchor="center")
    btn = Button(root, text="NOT Pleasantly!", width=30, height=5, bg="#FF5733", fg="black")

    def deletescreen(event):
        root.destroy()

    btn.bind("<Button-1>", deletescreen)
    btn.pack()
    root.mainloop()