# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 00:59:16 2018

@author: Валерия
"""

from tkinter import*
import random

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg = 'skyblue')
canv.pack(fill = BOTH, expand = 1)

def grass():
    x1 = 0
    for _ in range(1600):
        y2 = random.randint(585, 590)
        canv.create_rectangle(x1, 600, x1 + 1, y2, fill = 'green', outline = 'green')
        x1 += 0.5

def stone_ordinary(x, y):     
    canv.create_oval(x, y, x + 20, y - 10, fill = 'grey', outline = 'grey')

def stone_complicated(x, y):
    canv.create_oval(x, y, x + 40, y - 25, fill = 'grey', outline = 'grey')
    canv.create_oval(x + 2, y - 18, x + 7, y - 22, fill = 'grey', outline = 'grey')
    canv.create_oval(x + 7, y - 10, x + 35, y - 30, fill = 'grey', outline = 'grey')
    canv.create_oval(x + 15, y - 3, x + 37, y - 28, fill = 'grey', outline = 'grey')
    canv.create_oval(x + 28, y - 5, x + 42, y - 20, fill = 'grey', outline = 'grey')
    for _ in range (11):
        x1 = random.randint(x + 10, x + 33)
        y1 = random.randint(y - 20, y - 5)
        canv.create_oval(x1, y1, x1 + 2, y1 - 2, fill = 'black', outline = 'black')

canv.create_polygon((750, 600), (780, 400), (785, 430), (790, 330), (795, 290), (800, 340),
                    (800, 600), fill = 'brown', outline = 'brown')
canv.create_polygon((775, 433), (776, 438), (777, 435), (780, 437), (785, 430),
                    (780, 400), (775, 433), fill = 'white', outline = 'brown')
canv.create_polygon((788.5, 340), (795, 290), (800, 340), (790, 338), (789, 334), (788.5, 340), 
                    fill = 'white',
                    outline = 'brown')
grass()
stone_ordinary(50, 590)
stone_complicated(300, 590)
stone_ordinary(650, 593)
stone_complicated(100, 591)
stone_ordinary(250, 597)
stone_complicated(505, 597)
stone_ordinary(390, 590)
stone_ordinary(780, 590)
stone_ordinary(720, 594)
stone_ordinary(690, 593)

root.mainloop()
