# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 22:23:46 2018

@author: Валерия
"""

from tkinter import*

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)
GROUND_COLOR = 'white'

class Castle():
    pass

class Castle_1(Castle):
    def __init__(self):
        self.health = 100
        self.x = 250
        self.y = 250
        self.size_x = 50
        self.size_y = 20
        
    def draw_castle(self):
        for _ in range(2):
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                      self.y - self.size_y, fill = 'grey', outline = 'black')
                self.x += self.size_x
    
            self.x -= 2 * self.size_x
            self.y -= 2 * self.size_y
    
        self.y += 3 * self.size_y
    
        for _ in range(2):  
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + 0.5 * self.size_x, 
                                      self.y - self.size_y, fill = 'grey', outline = 'black')
                self.x += 1.5 * self.size_x
        
            self.x -= 3 * self.size_x
            self.y -= 2 * self.size_y
            
        self.x += 0.5 * self.size_x
        self.y += 4 * self.size_y
        canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                              self.y - self.size_y, fill = 'grey', outline = 'black')

class Castle_2(Castle):
    def __init__(self):
        self.health = 200
        self.x = 450
        self.y = 250
        self.size_x = 50
        self.size_y = 20
        
    def upgrade_1(self):
        for _ in range(3):
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                      self.y - self.size_y, fill = 'grey', outline = 'black')
                self.x += self.size_x
    
            self.x -= 2 * self.size_x
            self.y -= 2 * self.size_y
    
        self.y += 5 * self.size_y
    
        for _ in range(3):  
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + 0.5 * self.size_x, 
                                      self.y - self.size_y, fill = 'grey', outline = 'black')
                self.x += 1.5 * self.size_x
        
            self.x -= 3 * self.size_x
            self.y -= 2 * self.size_y
        
        self.x += 0.5* self.size_x
        self.y += 6 * self.size_y
    
        for _ in range(2): 
            canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                  self.y - self.size_y, fill = 'grey', outline = 'black')
            self.y -= 2 * self.size_y
    
        self.x -= 0.25 * self.size_x
        self.y -= self.size_y
    
        for _ in range(2):
            canv.create_line(self.x, self.y, self.x, self.y - 0.25 * self.size_y)
            canv.create_rectangle(self.x, self.y - 0.25 * self.size_y, 
                                  self.x + 0.2 * self.size_x, self.y - 0.5 * self.size_y, 
                                  fill = 'red', outline = 'red')
            self.x += 1.5 * self.size_x

class Castle_3(Castle):
    def __init__(self):
        self.health = 300
        self.x = 450
        self.y = 550
        self.size_x = 50
        self.size_y = 20
    
    def upgrade_2(self):
        for _ in range(3):
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                      self.y - self.size_y, fill = 'grey', 
                                      outline = 'black')
                self.x += self.size_x
    
            self.x -= 2 * self.size_x
            self.y -= 2 * self.size_y
    
        self.y += 5 * self.size_y
    
        for _ in range(3):  
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + 0.5 * self.size_x, 
                                      self.y - self.size_y, fill = 'grey', 
                                      outline = 'black')
                self.x += 1.5 * self.size_x
        
            self.x -= 3 * self.size_x
            self.y -= 2 * self.size_y
        
        self.x += 0.5 * self.size_x
        self.y += 6 * self.size_y
    
        for _ in range(2): 
            canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                  self.y - self.size_y, fill = 'grey', outline = 'black')
            self.y -= 2 * self.size_y
        
        self.x -= 0.25 * self.size_x
        self.y -= self.size_y
    
        for _ in range(2):
            canv.create_line(self.x, self.y, self.x, self.y - 0.25 * self.size_y)
            canv.create_rectangle(self.x, self.y - 0.25 * self.size_y, 
                                  self.x + 0.2 * self.size_x, self.y - 0.5 * self.size_y, 
                                  fill = 'red', outline = 'red')
            self.x += 1.5 * self.size_x
    
        self.x -= 4.75 * self.size_x
        self.y += 4 * self.size_y
    
        for _ in range(2):
            canv.create_oval(self.x, self.y, self.x + 1.5 * self.size_x, 
                             self.y - 2 * self.size_y, fill = 'grey', outline = 'black')
            self.y += 2 * self.size_y

            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                      self.y - self.size_y, fill = 'grey', outline = 'black')
                self.y -= 2 * self.size_y
    
            self.y += 4 * self.size_y
            self.x += self.size_x
        
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + 0.5 * self.size_x, 
                                      self.y - self.size_y, fill = 'grey', outline = 'black')
                self.y -= 2 * self.size_y
    
            self.y += 3 * self.size_y
            self.x -= self.size_x
            canv.create_rectangle(self.x, self.y, self.x + 0.5 * self.size_x, 
                                  self.y - self.size_y, fill = 'grey', outline = 'black')
            self.x += 0.5 * self.size_x
            canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                  self.y - self.size_y, fill = 'grey', outline = 'black')
            self.x += 3 * self.size_x
            self.y -= self.size_y

        
C1 = Castle_1()
C1.draw_castle()
C2 = Castle_2()
C2.upgrade_1()
C3 = Castle_3()
C3.upgrade_2()
root.mainloop()