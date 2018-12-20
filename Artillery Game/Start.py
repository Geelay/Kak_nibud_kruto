from tkinter import *
from Ground import *

root = Tk()
def Start():
    frame = Frame(root)
    root.overrideredirect(True)
    root.overrideredirect(False)
    root.attributes('-fullscreen', True)
    canv = Canvas(root, bg='white')
    canv.pack(fill=BOTH, expand=1)
    photo = PhotoImage(file="pushkagame.png")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    Label(root, image=photo).place(x=screen_width/2, y=screen_height/2, anchor="center")
    btn = Button(root, text="Start game", width=30, height=5, bg="#FF5733", fg="black")

    def deletescreen(event):
        root.destroy()
        game()

    btn.bind("<Button-1>", deletescreen)
    btn.pack()
    root.mainloop()

Start()
