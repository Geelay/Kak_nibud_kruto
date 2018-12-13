from tkinter import Tk, Frame, Menu
from tkinter import Button, RIGHT, TOP, FLAT, RAISED, X


class Shop(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Toolbar")

        menubar = Menu(self.parent)
        self.fileMenu = Menu(self.parent, tearoff=1)
        self.fileMenu.add_command(label="Новая игра")
        self.fileMenu.add_command(label="Справка")
        self.fileMenu.add_command(label="Выход", command=self.onExit)
        menubar.add_cascade(label="Файл", menu=self.fileMenu)

        toolbar = Frame(self.parent, bd=3, relief=RAISED)

        shieldbutton = Button(toolbar, text="ЗАЩИТА", relief=FLAT, width=10, height=6, font='arial 12', bg="#FF5733",
                              fg="#641E16", activebackground="#F4D03F")
        firebutton = Button(toolbar, text="ОРУЖИЕ", relief=FLAT, width=10, height=6, font='arial 12', bg="#FF5733",
                            fg="#641E16", activebackground="#F4D03F")
        powerupbutton = Button(toolbar, text="УЛУЧШЕНИЕ", relief=FLAT, width=10, height=6, font='arial 12',
                               bg="#FF5733",  fg="#641E16",  activebackground="#F4D03F")
        otherbutton = Button(toolbar, text="ПРОЧЕЕ", relief=FLAT, width=10, height=6, font='arial 12', bg="#FF5733",
                             fg="#641E16",  activebackground="#F4D03F")
        shieldbutton.pack(side=TOP, padx=2, pady=2)
        firebutton.pack(side=TOP, padx=2, pady=2)
        powerupbutton.pack(side=TOP, padx=2, pady=2)
        otherbutton.pack(side=TOP, padx=2, pady=2)

        toolbar.pack(side=RIGHT, fill=X)
        self.parent.config(menu=menubar)
        self.pack()

    def onExit(self):
        self.quit()


def main():
    root = Tk()
    root.geometry('1240x600+0+0')
    app = Shop(root)
    root.mainloop()


if __name__ == '__main__':
    main()