# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 14:48:26 2018

@author: Валерия
"""

from tkinter import*

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)
GROUND_COLOR = 'white'

class Protection():
    pass

class Termo_Protection(Protection):
    def __init__(self):
        self.x = 250
        self.y = 250
        self.radius = 40
        self.design = self.draw
        self.color = '#FFCC99'
        self.health = 10
    def draw(self):
        canv.create_oval((self.x, self.y), (self.x + 2 * self.radius, self.y + 2 * self.radius), 
                         fill = GROUND_COLOR, outline = self.color, width = 4)
        
class Energy_Protection(Protection):
    def __init__(self):
        self.x = 450
        self.y = 450
        self.radius = 60
        self.design = self.draw
        self.color = '#CCCCFF'
        self.health = 10
    def draw(self):
        canv.create_oval((self.x, self.y), (self.x + 2 * self.radius, self.y + 2 * self.radius), 
                         fill = GROUND_COLOR, outline = self.color, width = 4)

class Laser_Protection(Protection):
    def __init__(self):
        self.x = 450
        self.y = 250
        self.radius = 50
        self.design = self.draw
        self.color = '#FFDF84'
        self.health = 10
    def draw(self):
        canv.create_oval((self.x, self.y), (self.x + 2 * self.radius, self.y + 2 * self.radius), 
                         fill = GROUND_COLOR, outline = self.color, width = 4)
        
T = Termo_Protection()
E = Energy_Protection()
L = Laser_Protection()
E.draw()
T.draw()
L.draw()
root.mainloop()
