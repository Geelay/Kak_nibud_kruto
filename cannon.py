import math
import time 
from Classes import *
from tkinter import *

    
def up_handler(event):
    """
    Направляет дуло пушки в сторону курсора
    :param event: перемещение курсора по экрану
    :return: Координаты курсорв мыши
    """
    pushka.aim_up()

    
def down_handler(event):
    pushka.aim_down()

def shield(event):
    global defe, T, E, L
    defe += 1
    if defe == 1:
        E.draw()
    elif defe == 2:    
        T.draw()       
    elif defe == 3:
        L.draw()
        
        
T = Termo_Protection(gx, gy)
E = Energy_Protection(gx, gy)
L = Laser_Protection(gx, gy)
C1 = Castle(gx, gy)
C1.draw_castle()
pushka = Gun(gx, gy, 30, gun_number )

def cas_upgrade(event):
    global pushka, upg
    upg += 1
    if upg == 1:
        pushka.y -= 40
        pushka.y_f -= 40
        C1.upgrade_1()
    elif upg == 2:
        C1.upgrade_2()
    
def charge_inc(event):
    global charge
    charge += 1
    if charge > 10:
        charge = 0
    pushka.draw()
    
def change_gun(event):
    global gun_number, pushka
    pushka.delete_self()
    if gun_number < 4:
        gun_number += 1
    else:
        gun_number = 0
    pushka.number = gun_number


canv.bind("<Shift-MouseWheel>", charge_inc)
canv.bind("<1>", change_gun)      
canv.bind("<3>", cas_upgrade)  
canv.bind("<Alt-MouseWheel>", down_handler)
canv.bind("<Control-MouseWheel>", up_handler)
canv.bind("<2>", shield)
root.mainloop()
