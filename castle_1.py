# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 14:54:03 2018

@author: Валерия
"""

from tkinter import*

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)

def castle(x, y):
    for _ in range(2):
        for _ in range(2):
            canv.create_rectangle(x, y, x + 50, y - 20, fill = 'grey', outline = 'black')
            x += 50
    
        x -= 100
        y -= 40
    
    y += 60
    
    for _ in range(2):  
        for _ in range(2):
            canv.create_rectangle(x, y, x + 25, y - 20, fill = 'grey', outline = 'black')
            x += 75
        
        x -= 150
        y -= 40
        
    x += 25
    y += 80
    canv.create_rectangle(x, y, x + 50, y - 20, fill = 'grey', outline = 'black')
    

castle(300, 300)

canv.mainloop()
