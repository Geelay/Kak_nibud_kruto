from tkinter import *

root = Tk()
frame = Frame(root)
root.geometry('1200x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
photo = PhotoImage(file="pushkagame.png")
Label(root, image=photo).place(x=0, y=0)  # title
btn = Button(root,   text="Start game",  width=30, height=5, bg="#FF5733", fg="black")


def deletescreen(event):
    pass


btn.bind("<Button-1>", deletescreen)  # при нажатии ЛКМ на кнопку вызывается функция
btn.pack()  # расположить кнопку на главном окне
root.mainloop()
