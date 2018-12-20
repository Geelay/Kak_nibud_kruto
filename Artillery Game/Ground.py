from tkinter import *
import random



coordinate_x_stone_ordinary = [50, 197, 260, 330, 415, 500, 620, 705, 750, 810, 900, 1000, 1260]
"""координаты камней одного вида"""
coordinate_x_stone_complicated = [10, 100, 360, 560, 800, 1100, 1200, 1300, 1400, 1430, 1450, 1600, 1700]
"""координаты камней другого вида"""
cloud_distance_x = [25, 15, -25, -25, 0]
"""координаты смещения по Ox, используемые в функции рисования облака"""
cloud_distance_y = [0, 20, 0, 0, 0]
"""координаты смещения по Oy, используемые в функции рисования облака"""
coordinate_x_cloud = [100, 350, 600, 900, 1200]
"""начальные координаты облака по Ох"""
coordinate_y_cloud = [60, 100, 80, 55, 110]
"""начальные координаты облака по Оу"""


def game():
    root = Tk()
    frame = Frame(root)
    root.overrideredirect(True)
    root.overrideredirect(False)
    root.attributes('-fullscreen', True)
    canv = Canvas(root, bg='white')
    canv.pack(fill=BOTH, expand=1)
    photo = PhotoImage(file="backy.png")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    canv.create_image(screen_width / 2, screen_height / 2, image=photo, anchor=CENTER)

    def grass():
        x1 = 0
        canv.create_rectangle(0, 900, 1600, 700, fill='#3bad14', outline='#3bad14')
        for _ in range(2800):
            y2 = random.randint(685, 690)
            canv.create_rectangle(x1, 700, x1 + 0.5, y2, fill='#3bad14', outline='#3bad14')
            x1 += 0.5

    def rack(x, y):
        canv.create_polygon((x, y), (x + 80, y - 20), (x + 160, y - 20), (x + 240, y),
                            (x, y), fill='#677c5f', outline='#677c5f')

    def stone_ordinary(x, y):
        canv.create_oval(x, y, x + 20, y - 10, fill='grey', outline='grey')

    def stone_complicated(x, y):
        canv.create_oval(x, y, x + 40, y - 25, fill='grey', outline='grey')
        canv.create_oval(x + 2, y - 18, x + 7, y - 22, fill='grey', outline='grey')
        canv.create_oval(x + 7, y - 10, x + 35, y - 30, fill='grey', outline='grey')
        canv.create_oval(x + 15, y - 3, x + 37, y - 28, fill='grey', outline='grey')
        canv.create_oval(x + 28, y - 5, x + 42, y - 20, fill='grey', outline='grey')
        for _ in range(11):
            x1 = random.randint(x + 10, x + 33)
            y1 = random.randint(y - 20, y - 5)
            canv.create_oval(x1, y1, x1 + 2, y1 - 2, fill='black', outline='black')

    def mountain():
        canv.create_polygon((1200, 700), (1350, 200), (1400, 700), (1200, 700), fill='lemonchiffon4',
                            outline='lemonchiffon4')
        canv.create_polygon((1300, 367), (1350, 200), (1360, 310), (1350, 400), (1340, 370),
                            (1335, 390), (1330, 410), (1325, 400), (1320, 415), (1305, 385),
                            (1300, 367), fill='white', outline='lemonchiffon4')

    def cloud(x, y):
        for i in range(5):
            canv.create_oval((x, y), (x + 30, y - 30), fill='white', outline='white')
            x += cloud_distance_x[i]
            y += cloud_distance_y[i]

    def menu():
        menubar = Menu(root)
        root.config(menu=menubar)
        filemenu = Menu(root, tearoff=1)
        filemenu.add_command(label="Новая игра")
        filemenu.add_command(label="Справка")
        filemenu.add_command(label="Выход", command=root.quit)
        menubar.add_cascade(label="Файл", menu=filemenu)

    def toolbar():
        bottomframe = Frame(root)
        bottomframe.pack(side=BOTTOM)

        h = 1

        shieldbutton = Button(bottomframe, text="ЗАЩИТА", relief=FLAT, width=30, height=h, font='arial 12',
                              bg="#FF5733", fg="#641E16", highlightcolor="#CB4335", activebackground="#F4D03F")
        firebutton = Button(bottomframe, text="ОРУЖИЕ", relief=FLAT, width=30, height=h, font='arial 12', bg="#FF5733",
                            fg="#641E16",  highlightcolor="#CB4335", activebackground="#F4D03F")
        powerbutton = Button(bottomframe, text="УЛУЧШЕНИЕ", relief=FLAT, width=30, height=h, font='arial 12',
                             bg="#FF5733",  fg="#641E16", highlightcolor="#CB4335", activebackground="#F4D03F")
        otherbutton = Button(bottomframe, text="ПРОЧЕЕ", relief=FLAT, width=30, height=h, font='arial 12', bg="#FF5733",
                             fg="#641E16",  highlightcolor="#CB4335", activebackground="#F4D03F")
        shieldbutton.pack(side=LEFT, padx=2, pady=2)
        firebutton.pack(side=LEFT, padx=2, pady=2)
        powerbutton.pack(side=LEFT, padx=2, pady=2)
        otherbutton.pack(side=LEFT, padx=2, pady=2)

    def firetablet():
        upperframe = Frame(root)
        upperframe.place(x=2, y=2)

        up_btn = Button(upperframe, text="Up", width=9, height=4, font='arial 12', bg="#FF5733", fg="#641E16",
                        activebackground="#F4D03F")
        fire_btn = Button(upperframe, text="Fire", width=9, height=4, font='arial 12', bg="#FF5733", fg="#641E16",
                          activebackground="#F4D03F")
        down_btn = Button(upperframe, text="Down", width=9, height=4, font='arial 12', bg="#FF5733", fg="#641E16",
                          activebackground="#F4D03F")
        up_btn.pack(side=TOP)
        fire_btn.pack(side=TOP)
        down_btn.pack(side=TOP)

    def main():

        toolbar()
        firetablet()
        mountain()
        grass()
        rack(30, 690)
        rack(1000, 690)
        menu()

        for i in range(13):
            stone_ordinary(coordinate_x_stone_ordinary[i], random.randint(697, 760))
            stone_complicated(coordinate_x_stone_complicated[i], random.randint(697, 760))
        for i in range(5):
            cloud(coordinate_x_cloud[i], coordinate_y_cloud[i])

    main()

    root.mainloop()

