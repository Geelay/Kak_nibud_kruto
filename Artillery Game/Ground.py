# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 00:59:16 2018
@author: Валерия
"""

from tkinter import *
import random

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
canv.create_image(screen_width/2, screen_height/2, image=photo, anchor=CENTER)


coordinate_x_stone_ordinary = [50, 197, 260, 620, 705, 900, 1000]
"""координаты камней одного вида"""
coordinate_x_stone_complicated = [100, 350, 560, 800, 1100, 1200, 1300]
"""координаты камней другого вида"""
cloud_distance_x = [25, 15, -25, -25, 0]
"""координаты смещения по Ox, используемые в функции рисования облака"""
cloud_distance_y = [0, 20, 0, 0, 0]
"""координаты смещения по Oy, используемые в функции рисования облака"""
coordinate_x_cloud = [100, 350, 600, 900, 1200]
"""начальные координаты облака по Ох"""
coordinate_y_cloud = [60, 100, 80, 55, 110]
"""начальные координаты облака по Оу"""


def grass():
    x1 = 0
    for _ in range(2800):
        y2 = random.randint(685, 690)
        canv.create_rectangle(x1, 700, x1 + 1, y2, fill='green', outline='green')
        x1 += 0.5


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


def sun():
    canv.create_oval((1250, 90), (1500, -90), fill='gold', outline='gold')


def mountain():
    canv.create_polygon((1200, 700), (1350, 200), (1400, 700), (1200, 700), fill='lemonchiffon4',
                        outline='lemonchiffon4')
    canv.create_polygon((1300, 367), (1350, 200), (1360, 310), (1350, 400), (1340, 370),
                        (1335, 390), (1330, 410), (1325, 400), (1320, 415), (1305, 385),
                        (1300, 367), fill='white', outline='lemonchiffon4')
    canv.create_oval((1250, 90), (1500, -90), fill='gold', outline='gold')


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


def main():
    mountain()
    grass()
    sun()
    menu()

    for i in range(7):
        stone_ordinary(coordinate_x_stone_ordinary[i], random.randint(690, 697))
        stone_complicated(coordinate_x_stone_complicated[i], random.randint(690, 697))

    for i in range(5):
        cloud(coordinate_x_cloud[i], coordinate_y_cloud[i])


main()
root.mainloop()
