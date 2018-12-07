# from pil import Image, ImageTk
from tkinter import Tk, Frame, Menu
from tkinter import Button, LEFT, RIGHT, TOP, Y, FLAT, RAISED, X


class Shop(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Toolbar")

        menubar = Menu(self.parent)
        self.fileMenu = Menu(self.parent, tearoff=1)
        self.fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=self.fileMenu)

        toolbar = Frame(self.parent, bd=1, relief=RAISED)

        shieldbutton = Button(toolbar, text="ЗАЩИТА", relief=FLAT, width=10, height=6)
        firebutton = Button(toolbar, text="ОРУЖИЕ", relief=FLAT, width=10, height=6)
        powerupbutton = Button(toolbar, text="УЛУЧШЕНИЕ", relief=FLAT, width=10, height=6)
        otherbutton = Button(toolbar, text="ПРОЧЕЕ", relief=FLAT, width=10, height=6)
        shieldbutton.pack(side=TOP, padx=1, pady=1)
        firebutton.pack(side=TOP, padx=1, pady=1)
        powerupbutton.pack(side=TOP, padx=1, pady=1)
        otherbutton.pack(side=TOP, padx=1, pady=1)

        toolbar.pack(side=RIGHT, fill=X)
        self.parent.config(menu=menubar)
        self.pack()

    def onExit(self):
        self.quit()


def main():
    root =Tk()
    root.geometry("250x150+300+300")
    app = Shop(root)
    root.mainloop()


if __name__ == '__main__':
    main()