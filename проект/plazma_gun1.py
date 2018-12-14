import time
from tkinter import *
charge = 0
root = Tk()
root.geometry('800x600')
GROUND_COLOR = 'white'
canv = Canvas(root, bg = GROUND_COLOR)
canv.pack(fill = BOTH, expand = 1)

def plazma_gun1(x, y, r):

    canv.create_rectangle (x + r/2, y + 0.2 * r , x + 2*r, y + 0.8 * r, fill = '#543964', width = 2)
    canv.create_oval(x, y, x + r, y + r, fill = '#543964', width = 2)
    canv.create_oval(x+r/4, y+r/4, x + 3*r/4, y + 3*r/4, fill = GROUND_COLOR, outline = '#543964')
    canv.create_rectangle (x + 1.2*r, y + 0.45 * r , x + 1.7 * r, y + 0.55 * r, fill = GROUND_COLOR, outline = '#543964' )

def plazma_ball(x, y, r):
    canv.create_oval (x + 2 * r, y + 0.2 * r, x + 2.6 * r, y+ 0.8 * r, fill = '#32127A', outline = '#32127A' )
    
def shoot(x, y, r):
    global charge
    canv.delete(ALL)
    plazma_gun1(x, y, r)
    canv.create_rectangle (x + 1.2 * r, y + 0.45 * r , x + 1.2 * r + 0.05 * r * charge, y + 0.55 * r, fill = '#122FAA', outline = '#543964' )
    if charge > 9:
        charge = 0
    else:
        charge += 1
    if charge == 10:
        plazma_ball(x, y, r)
        
        
def time_handler():
    shoot(300, 300, 100)
    root.after(100 , time_handler)
root.after(10, time_handler)
canv.mainloop()
