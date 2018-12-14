# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 23:58:06 2018

@author: Валерия
"""

from tkinter import*

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)

def castle(x, y):
    for _ in range(3):
        for _ in range(2):
            canv.create_rectangle(x, y, x + 50, y - 20, fill = 'grey', outline = 'black')
            x += 50
    
        x -= 100
        y -= 40
    
    y += 100
    
    for _ in range(3):  
        for _ in range(2):
            canv.create_rectangle(x, y, x + 25, y - 20, fill = 'grey', outline = 'black')
            x += 75
        
        x -= 150
        y -= 40
        
    x += 25
    y += 120
    
    for _ in range(2): 
        canv.create_rectangle(x, y, x + 50, y - 20, fill = 'grey', outline = 'black')
        y -= 40
    
    x -= 12.5
    y -= 20
    
    for _ in range(2):
        canv.create_line(x, y, x, y - 5)
        canv.create_rectangle(x, y - 5, x + 10, y - 10, fill = 'red', outline = 'red')
        x += 75
    
castle(300, 300)

canv.mainloop()