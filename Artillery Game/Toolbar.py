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
                              fg="#641E16", highlightcolor="#CB4335", activebackground="#F4D03F")
        firebutton = Button(toolbar, text="ОРУЖИЕ", relief=FLAT, width=10, height=6, font='arial 12', bg="#FF5733",
                            fg="#641E16",  highlightcolor="#CB4335", activebackground="#F4D03F")
        powerbutton = Button(toolbar, text="УЛУЧШЕНИЕ", relief=FLAT, width=10, height=6, font='arial 12',
                             bg="#FF5733",  fg="#641E16", highlightcolor="#CB4335", activebackground="#F4D03F")
        otherbutton = Button(toolbar, text="ПРОЧЕЕ", relief=FLAT, width=10, height=6, font='arial 12', bg="#FF5733",
                             fg="#641E16",  highlightcolor="#CB4335", activebackground="#F4D03F")
        shieldbutton.pack(side=TOP, padx=2, pady=2)
        firebutton.pack(side=TOP, padx=2, pady=2)
        powerbutton.pack(side=TOP, padx=2, pady=2)
        otherbutton.pack(side=TOP, padx=2, pady=2)

        toolbar.pack(side=RIGHT, fill=X)
        self.parent.config(menu=menubar)
        self.pack()

        def shieldbutton_click(event):     # сюда нужно внести функции, меняющие свойства замка и оружия #TODO
            print ("установить защиту")

        def firebutton_click(event):
            print ("выбрать оружие")

        def powerbutton_click(event):
            print ("применить улучшение")

        def otherbutton_click(event):
            print ("открыть другие возможности")

        shieldbutton.bind("<Button-1>", shieldbutton_click)
        firebutton.bind("<Button-1>", firebutton_click)
        powerbutton.bind("<Button-1>", powerbutton_click)
        otherbutton.bind("<Button-1>", otherbutton_click)

    def onExit(self):
        self.quit()


def main():
    root = Tk()
    root.overrideredirect(True)
    root.overrideredirect(False)
    root.attributes('-fullscreen', True)
    app = Shop(root)
    root.mainloop()


if __name__ == '__main__':
    main()
