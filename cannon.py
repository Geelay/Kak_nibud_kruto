import math
import time 
import random
import start
from tkinter import *
start.start()
upg = 0
upp = 0
motion = 0
charge = 0
enemy_charge = 9
shellcolor = 'black'
enemy_shellcolor = 'black'
G = - 98
money = 100
time = 10
gx = 130
gy = 600 

gr = 50
defe = 0

root = Tk()
root.overrideredirect(True) 
root.overrideredirect(False) 
root.attributes('-fullscreen', True)
GROUND_COLOR = 'white'
canv = Canvas(root, bg = '#7FC7FF')
canv.pack(fill = BOTH, expand = 1)
gun_number = 0
photo = PhotoImage(file="backy.png")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
canv.create_image(screen_width / 2, screen_height / 2.5, image=photo, anchor=CENTER)
menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(root, tearoff=1)
filemenu.add_command(label="Новая игра")
filemenu.add_command(label="Справка")
filemenu.add_command(label="Выход", command=root.quit)
menubar.add_cascade(label="Файл", menu=filemenu)

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



def grass():
        x1 = 0
        canv.create_rectangle(0, 900, 1600, 700, fill='#3bad14', outline='#3bad14')
        for _ in range(3500):
            y2 = random.randint(685, 690)
            canv.create_rectangle(x1, 700, x1 + 0.5, y2, fill='#3bad14', outline='#3bad14')
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

def mountain():
        canv.create_polygon((1200, 700), (1350, 200), (1400, 700), (1200, 700), fill='lemonchiffon4',
                            outline='lemonchiffon4')
        canv.create_polygon((1300, 367), (1350, 200), (1360, 310), (1350, 400), (1340, 370),
                            (1335, 390), (1330, 410), (1325, 400), (1320, 415), (1305, 385),
                            (1300, 367), fill='white', outline='lemonchiffon4')
        canv.create_polygon((1000, 700), (1150, 200), (1200, 700), (1000, 700), fill='lemonchiffon4',
                            outline='lemonchiffon4')
        canv.create_polygon((1100, 367), (1150, 200), (1160, 310), (1150, 400), (1140, 370),
                            (1135, 390), (1130, 410), (1125, 400), (1120, 415), (1105, 385),
                            (1100, 367), fill='white', outline='lemonchiffon4')
        canv.create_polygon((1100, 700), (1250, 200), (1300, 700), (1100, 700), fill='lemonchiffon4',
                            outline='black')
        canv.create_polygon((1200, 367), (1250, 200), (1260, 310), (1250, 400), (1240, 370),
                            (1235, 390), (1230, 410), (1225, 400), (1220, 415), (1205, 385),
                            (1200, 367), fill='white', outline='lemonchiffon4')
def cloud(x, y):
        for i in range(5):
            canv.create_oval((x, y), (x + 30, y - 30), fill='white', outline='white')
            x += cloud_distance_x[i]
            y += cloud_distance_y[i]





class Protection():
    pass
class None_protection(Protection):
    def __init__(self, x, y):
        self.x = x + 150 - 280 
        self.y = y + 50 - 160
        self.radius = 150
        self.design = self.draw
        self.color = '#FFFFFF'
        self.health = 10
        
    def draw(self):
        canv.create_oval((self.x, self.y), (self.x + 2 * self.radius, self.y + 2 * self.radius),
                         fill='', outline='', width=4)
        
class Termo_Protection(Protection):
    def __init__(self, x, y):
        self.x = x + 150 - 280 
        self.y = y + 50 - 160
        self.radius = 150
        self.design = self.draw
        self.color = '#92000A'
        self.health = 10

    def draw(self):
        canv.create_oval((self.x, self.y), (self.x + 2 * self.radius, self.y + 2 * self.radius),
                         fill='', outline=self.color, width=4)


class Energy_Protection(Protection):
    def __init__(self, x, y):
        self.x = x + 150 - 280
        self.y = y + 50 - 160
        self.radius = 150
        self.design = self.draw
        self.color = '#1B5583'
        self.health = 10

    def draw(self):
        canv.create_oval((self.x, self.y), (self.x + 2 * self.radius, self.y + 2 * self.radius),
                         fill='', outline=self.color, width=4)


class Laser_Protection(Protection):
    def __init__(self, x, y):
        self.x = x + 150 - 280
        self.y = y + 50 - 160
        self.radius = 150
        self.design = self.draw
        self.color = '#B8860B'
        self.health = 10

    def draw(self):
        canv.create_oval((self.x, self.y), (self.x + 2 * self.radius, self.y + 2 * self.radius),
                         fill='', outline=self.color, width=4)



class Castle():
    def __init__(self, x, y, r):
        self.health = 100
        self.healthful = 100
        self.x = x - 30
        self.y = y + 90
        self.size_x = r
        self.size_y = r / 50 * 20
        
    def draw_castle(self):
        for _ in range(2):
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                      self.y - self.size_y, fill = '#8A9597', outline = 'black')
                self.x += self.size_x
    
            self.x -= 2 * self.size_x
            self.y -= 2 * self.size_y
    
        self.y += 3 * self.size_y
    
        for _ in range(2):  
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + 0.5 * self.size_x, 
                                      self.y - self.size_y, fill = '#8A9597', outline = 'black')
                self.x += 1.5 * self.size_x
        
            self.x -= 3 * self.size_x
            self.y -= 2 * self.size_y
            
        self.x += 0.5 * self.size_x
        self.y += 4 * self.size_y
        canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                              self.y - self.size_y, fill = '#8A9597', outline = 'black')



        
    def upgrade_1(self, x, y, r):
        self.health = 200
        self.healthful = self.healthful + 100
        self.x = x - 30
        self.y = y + 90
        self.size_x = r
        self.size_y = r / 50 * 20
        for _ in range(3):
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                      self.y - self.size_y, fill = '#708090', outline = 'black')
                self.x += self.size_x
    
            self.x -= 2 * self.size_x
            self.y -= 2 * self.size_y
    
        self.y += 5 * self.size_y
    
        for _ in range(3):  
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + 0.5 * self.size_x, 
                                      self.y - self.size_y, fill = '#708090', outline = 'black')
                self.x += 1.5 * self.size_x
        
            self.x -= 3 * self.size_x
            self.y -= 2 * self.size_y
        
        self.x += 0.5* self.size_x
        self.y += 6 * self.size_y
    
        for _ in range(2): 
            canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                  self.y - self.size_y, fill = '#708090', outline = 'black')
            self.y -= 2 * self.size_y
    
        self.x -= 0.25 * self.size_x
        self.y -= self.size_y
    
        for _ in range(2):
            canv.create_line(self.x, self.y, self.x, self.y - 0.25 * self.size_y)
            canv.create_rectangle(self.x, self.y - 0.25 * self.size_y, 
                                  self.x + 0.2 * self.size_x, self.y - 0.5 * self.size_y, 
                                  fill = 'red', outline = 'red')
            self.x += 1.5 * self.size_x

    def upgrade_2(self, x, y, r):
        self.health = 300
        self.healthful = self.healthful + 100
        self.x = x - 30
        self.y = y + 90
        self.size_x = r
        self.size_y = r / 50 * 20
        for _ in range(3):
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                      self.y - self.size_y, fill = '#4C5866', 
                                      outline = 'black')
                self.x += self.size_x
    
            self.x -= 2 * self.size_x
            self.y -= 2 * self.size_y
    
        self.y += 5 * self.size_y
    
        for _ in range(3):  
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + 0.5 * self.size_x, 
                                      self.y - self.size_y, fill = '#4C5866', 
                                      outline = 'black')
                self.x += 1.5 * self.size_x
        
            self.x -= 3 * self.size_x
            self.y -= 2 * self.size_y
        
        self.x += 0.5 * self.size_x
        self.y += 6 * self.size_y
    
        for _ in range(2): 
            canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                  self.y - self.size_y, fill = '#4C5866', outline = 'black')
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
                             self.y - 2 * self.size_y, fill = '#4C5866', outline = 'black')
            self.y += 2 * self.size_y

            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                      self.y - self.size_y, fill = '#4C5866', outline = 'black')
                self.y -= 2 * self.size_y
    
            self.y += 4 * self.size_y
            self.x += self.size_x
        
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + 0.5 * self.size_x, 
                                      self.y - self.size_y, fill = '#4C5866', outline = 'black')
                self.y -= 2 * self.size_y
    
            self.y += 3 * self.size_y
            self.x -= self.size_x
            canv.create_rectangle(self.x, self.y, self.x + 0.5 * self.size_x, 
                                  self.y - self.size_y, fill = '#4C5866', outline = 'black')
            self.x += 0.5 * self.size_x
            canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                  self.y - self.size_y, fill = '#4C5866', outline = 'black')
            self.x += 3 * self.size_x
            self.y -= self.size_y
            
    def upgrade_3(self, x, y, r):
        self.health = 500
        self.healthful = self.healthful + 200
        self.x = x - 30
        self.y = y + 90
        self.size_x = r
        self.size_y = r / 50 * 20
        for _ in range(3):
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                      self.y - self.size_y, fill = '#FFD700', 
                                      outline = 'black')
                self.x += self.size_x
    
            self.x -= 2 * self.size_x
            self.y -= 2 * self.size_y
    
        self.y += 5 * self.size_y
    
        for _ in range(3):  
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + 0.5 * self.size_x, 
                                      self.y - self.size_y, fill = '#FFD700', 
                                      outline = 'black')
                self.x += 1.5 * self.size_x
        
            self.x -= 3 * self.size_x
            self.y -= 2 * self.size_y
        
        self.x += 0.5 * self.size_x
        self.y += 6 * self.size_y
    
        for _ in range(2): 
            canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                  self.y - self.size_y, fill = '#FFD700', outline = 'black')
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
                             self.y - 2 * self.size_y, fill = '#FFD700', outline = 'black')
            self.y += 2 * self.size_y

            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                      self.y - self.size_y, fill = '#FFD700', outline = 'black')
                self.y -= 2 * self.size_y
    
            self.y += 4 * self.size_y
            self.x += self.size_x
        
            for _ in range(2):
                canv.create_rectangle(self.x, self.y, self.x + 0.5 * self.size_x, 
                                      self.y - self.size_y, fill = '#FFD700', outline = 'black')
                self.y -= 2 * self.size_y
    
            self.y += 3 * self.size_y
            self.x -= self.size_x
            canv.create_rectangle(self.x, self.y, self.x + 0.5 * self.size_x, 
                                  self.y - self.size_y, fill = '#FFD700', outline = 'black')
            self.x += 0.5 * self.size_x
            canv.create_rectangle(self.x, self.y, self.x + self.size_x, 
                                  self.y - self.size_y, fill = '#FFD700', outline = 'black')
            self.x += 3 * self.size_x
            self.y -= self.size_y
        


class Shell:
    def __init__(self, x, y, r, vx, vy, direction, shellcolor):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.direction = direction
        self.size = r
        self.delta_x = 0
        self.delta_y = 0
        self.color = shellcolor
        self.canvas = canv
        self.oval = canv.create_oval (self.x + 2 * self.size, self.y + 0.2 * self.size, self.x + 2.6 * self.size, self.y+ 0.8 * self.size, fill=self.color, outline=self.color )

    def go(self, dt):
        """
        Сдвигает снаряд исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt: время элементарного перемещения
        :return: Движущийся снаряд
        """

        ax, ay = 0, G
        self.delta_x = self.vx * dt * math.cos(self.direction) + ax * (dt ** 2) / 2
        self.delta_y = self.vy * dt * math.sin(self.direction) + ay * (dt ** 2) / 2
        self.x += self.delta_x
        self.y += self.delta_y
        self.vx += ax * dt
        self.vy += -ay * dt
        self.draw()

        

    def draw(self):
        """
        Рисует движущийся снаряд
        :return:
        """
        self.canvas.move(self.oval, self.delta_x, self.delta_y)

    def detect_collision(self, other):
        """
        Проверяет факт соприкосновения снаряда и объекта other
        :param other: объект, который должен иметь поля x, y, r
        :return: логическое значение типа bool
        """
        pass
    def destroy(self):
        canv.delete(self.oval)
        

    def hit_checker(self):
        if self.x > 1200 and self.x < 1350 and self.y > 600 and self.y < 700:
            self.destroy()
            self.x = 10000
            self.y = 10000
            return(True) 

    def enemy_hit(self):
        if self.x < 140 and self.x > 0:
            self.destroy()
            self.x = -10000
            self.y = 10000
            return(True)        

class Gun:
    def __init__(self, x, y, size, number):
        self.canvas = canv
        self.x = x
        self.y = y
        self.size = size
        self.direction = 0
        self.y_f = self.y 
        self.x_f = self.x 
        self.line1 = canv.create_line(0,0,0,0)
        self.line2 = canv.create_line(0,0,0,0)
        self.line3 = canv.create_line(0,0,0,0)
        self.number = number


        
    def aim_up(self):
        global motion
        self.direction += self.size*math.pi/4400
        self.y_f -= math.cos(self.direction)
        self.x_f -= math.sin(self.direction)
        self.draw()
        if motion == 1:
            root.after(10, self.aim_up) 
    def aim_down(self):
        global motion
        self.direction -= self.size*math.pi/4400
        self.y_f += math.cos(self.direction)
        self.x_f += math.sin(self.direction)
        self.draw()
        if motion == 1:
            root.after(10, self.aim_down) 
    def gun_line(self):
        """
        Рисует дуло пушки
        """
 
        
        self.line1 = canv.create_line (self.x + self.size / 2, self.y + 0.5 * self.size , self.x_f + 2 * self.size, self.y_f + 0.5 * self.size, fill = '#543964', width = 0.6 * self.size)
        
        self.line3 = canv.create_line (self.x + 1.2 * self.size, self.y + 0.9 * self.size , self.x + 1.2 * self.size + 0.05 * self.size * charge, self.y + 0.9 * self.size, fill = '#122FAA', width = 0.1 * self.size)
    def gun_shell(self):
        """
        Рисует пушку без дула
        """
        
        canv.create_oval(self.x, self.y, self.x + self.size, self.y + self.size, fill = '#543964', width = 2)
        if self.number == 0:
            canv.create_oval(self.x + self.size/4, self.y + self.size/4, self.x + 3 * self.size/4, self.y + 3 * self.size/4, fill = GROUND_COLOR, outline = '#543964')
        elif self.number == 1:
            canv.create_oval(self.x + self.size/4, self.y + self.size/4, self.x + 3 * self.size/4, self.y + 3 * self.size/4, fill = '#E28B00', outline = '#543964')
        elif self.number == 2:
            canv.create_oval(self.x + self.size/4, self.y + self.size/4, self.x + 3 * self.size/4, self.y + 3 * self.size/4, fill = '#75151E', outline = '#543964')
        elif self.number == 3:
            canv.create_oval(self.x + self.size/4, self.y + self.size/4, self.x + 3 * self.size/4, self.y + 3 * self.size/4, fill = '#191970', outline = '#543964')
            
      
    def draw(self):
        self.canvas.delete(self.line1)
        self.canvas.delete(self.line2)
        self.canvas.delete(self.line3) 
        self.gun_line()
        self.gun_shell()

        
        


    def fire(self):
        """
        Создаёт объект снаряда (если ещё не потрачены все снаряды)
        летящий в направлении угла direction
        со скоростью, зависящей от длительности клика мышки
        :return: экземпляр снаряда типа Shell
        """
        shell.draw
        pass

    def delete_self(self):
        self.canvas.delete(self.line1)
        self.canvas.delete(self.line2)
        self.canvas.delete(self.line3) 
    
def up_handler(event):
    global motion
    motion = 1
    pushka.aim_up()

    
def down_handler(event):
    global motion
    motion = 1
    pushka.aim_down()
    

def shield_t(event):
    global shield, balan, money
    if money > 49:
        shield = Termo_Protection(gx, gy)
        shield.draw()
        money -= 50
        canv.delete(balan)
        balan = canv.create_text(screen_width/2, 50, text= str(money) + '☫', font='Arial 50')        
def shield_l(event):
    global shield, balan, money
    if money > 49:
        shield = Laser_Protection(gx, gy)
        shield.draw()
        money -= 50
        canv.delete(balan)
        balan = canv.create_text(screen_width/2, 50, text= str(money) + '☫', font='Arial 50')    
def shield_e(event):
    global shield, balan, money
    if money > 49:
        shield = Energy_Protection(gx, gy)
        shield.draw()
        money -= 50
        canv.delete(balan)
        balan = canv.create_text(screen_width/2, 50, text= str(money) + '☫', font='Arial 50')    
             

def cas_upgrade(event):
    global pushka, upg, money, balan
    if money > 99:
        upg += 1
        if upg == 1:
            pushka.y -= gr /50 * 40
            pushka.y_f -= gr /50 * 40
            pushka.draw()
            C1.upgrade_1(gx, gy, gr)
        elif upg == 2:
            C1.upgrade_2(gx, gy, gr)
        elif upg == 3:
            C1.upgrade_3(gx, gy, gr)
        money -= 100
        canv.delete(balan)
        balan = canv.create_text(screen_width/2, 50, text= str(money) + '☫', font='Arial 50')
def charge_inc(event):
    global charge, speed_scale
    charge = speed_scale.get()
    pushka.draw()
    
  
def shoot(event):
    global shell, time, money, balan, pushka
    if pushka.number != 0:
        money -= 50
        canv.delete(balan)
        balan = canv.create_text(screen_width/2, 50, text= str(money) + '☫', font='Arial 50')        
    time += 10
    shell.destroy()
    shell = Shell(pushka.x_f, pushka.y_f, 30, charge*40*math.cos(pushka.direction),  -charge*40*math.sin(pushka.direction), pushka.direction,shellcolor)
    fly()
    enemy_turn()
    
def enemyshoot():
    global enemy_shell, time, enemy_shellcolor
    time += 10
    enemy_shell.destroy()
    enemy_shell = Shell(enemy_pushka.x_f, enemy_pushka.y_f, 30, -enemy_charge*40*math.cos(enemy_pushka.direction),  -enemy_charge*40*math.sin(enemy_pushka.direction), enemy_pushka.direction, enemy_shellcolor)
    enemy_shell.color = enemy_shellcolor
    enemy_fly()
def hit_castle():
    global enemy_castle, hp, zash
    if pushka.number != zash and pushka.number != 0:
        canv.delete(hp)  
        enemy_castle.healthful -= 50
        hp = canv.create_text(1350, 650, text= str(enemy_castle.healthful) + '/' + str(enemy_castle.health), font='Arial 15', fill = '#B00000')
        if enemy_castle.healthful < 1:
            root.destroy()
            start.finish1()
            
def fly():
    global shell, enemy_castle
    shell.go(0.02)
    if shell.hit_checker() == True:
        print('hit')
        hit_castle()
    root.after(time, fly)   

def enemy_fly():
    enemy_shell.go(0.02)
    selfhit()
    root.after(time, enemy_fly) 
    
def k_gunup(event):
    global gun_number, pushka, shellcolor, money, balan
    if money > 49:
        shellcolor = '#CCA817'
        gun_number = 1
        pushka.delete_self()
        pushka.number = gun_number
        pushka.draw()
        money -= 50
        canv.delete(balan)
        balan = canv.create_text(screen_width/2, 50, text= str(money) + '☫', font='Arial 50') 
def t_gunup(event):
    global gun_number, pushka, shellcolor, money, balan
    if money > 49:
        shellcolor = '#7F180D'
        gun_number = 2
        pushka.delete_self()
        pushka.number = gun_number
        pushka.draw()
        money -= 50
        canv.delete(balan)
        balan = canv.create_text(screen_width/2, 50, text= str(money) + '☫', font='Arial 50') 
def e_gunup(event):
    global gun_number, pushka, shellcolor, money, balan
    if money > 49:
        shellcolor = '#32127A'
        gun_number = 3
        pushka.delete_self()
        pushka.number = gun_number
        pushka.draw()
        money -= 50
        canv.delete(balan)
        balan = canv.create_text(screen_width/2, 50, text= str(money) + '☫', font='Arial 50') 
def gold(event):
    global money, balan
    money += 100
    canv.delete(balan)
    balan = canv.create_text(screen_width/2, 50, text= str(money) + '☫', font='Arial 50') 
def selfhit():
    global C1, enemy_pushka, shield, shp, enemy_shell
    if enemy_shell.enemy_hit() == True:
        if shield.color == '#FFFFFF':
            canv.delete(shp) 
            C1.healthful -= 50
            shp = canv.create_text(150, 650, text= str(C1.healthful) + '/' + str(C1.health), font='Arial 15', fill = '#B00000')
            if C1.healthful < 1:
                root.destroy()
                start.finish2()            
        if shield.color != '#B8860B' and enemy_pushka.number == 1:
            canv.delete(shp) 
            C1.healthful -= 50
            shp = canv.create_text(150, 650, text= str(C1.healthful) + '/' + str(C1.health), font='Arial 15', fill = '#B00000')
            if C1.healthful < 1:
                root.destroy()
                start.finish2()

        if shield.color != '#92000A' and enemy_pushka.number == 2:
            canv.delete(shp) 
            C1.healthful -= 50
            shp = canv.create_text(150, 650, text= str(C1.healthful) + '/' + str(C1.health), font='Arial 15', fill = '#B00000')
            if C1.healthful < 1:
                root.destroy()
                start.finish2()

        if shield.color != '#1B5583' and enemy_pushka.number == 3: 
            canv.delete(shp) 
            C1.healthful -= 50
            shp = canv.create_text(150, 650, text= str(C1.healthful) + '/' + str(C1.health), font='Arial 15', fill = '#B00000')
            if C1.healthful < 1:
                root.destroy()
                start.finish2()


def enemy_turn():
    global upp, enemy_castle, enemy_pushka, enemy_shellcolor, enemy_shield, money, balan, zash, pushka
    zash = random.randint(1, 3)
    if zash == 2:
        enemy_shield = Termo_Protection(gx+1200, gy)
    elif zash == 1:
        enemy_shield = Laser_Protection(gx+1200, gy)
    elif zash == 3:
        enemy_shield = Energy_Protection(gx+1200, gy)
    enemy_shield.draw()
    enemy_pushka.number = random.randint(0, 3)
    if enemy_pushka.number == 0:
        enemy_shellcolor = 'black'
    elif enemy_pushka.number == 1:
        enemy_shellcolor = '#CCA817'
    elif enemy_pushka.number == 2:
        enemy_shellcolor = '#7F180D'
    elif enemy_pushka.number == 3:
        enemy_shellcolor = '#32127A'         
    enemy_pushka.draw()
    upp += 1
    if upp == 5:
        enemy_castle.upgrade_1(gx+1200, gy, gr)
        enemy_pushka.delete_self()
        enemy_pushka.y -= gr /50 * 40
        enemy_pushka.y_f -= gr /50 * 40
        enemy_pushka.draw()
    elif upp == 10:
        enemy_castle.upgrade_2(gx+1200, gy, gr)
    elif upp == 15:
        enemy_castle.upgrade_3(gx+1200, gy, gr)
    enemyshoot()
    money += 100
    canv.delete(balan)
    balan = canv.create_text(screen_width/2, 50, text= str(money) + '☫', font='Arial 50')



    
def stop_motion(event):
    global motion
    motion = 0
    
def toolbar():
        bottomframe = Frame(root)
        bottomframe.pack(side=BOTTOM)

        h = 1

        shieldbutton = Button(bottomframe, text="SHIELDS", relief=FLAT, width=30, height=h, font='arial 15',
                              bg="#FF5733", fg="#641E16", highlightcolor="#CB4335", activebackground="#F4D03F")
        firebutton = Button(bottomframe, text="WEAPONS", relief=FLAT, width=30, height=h, font='arial 15', bg="#FF5733",
                            fg="#641E16",  highlightcolor="#CB4335", activebackground="#F4D03F")
        powerbutton = Button(bottomframe, text="UPGRADE  (100☫)", relief=FLAT, width=30, height=h, font='arial 15',
                             bg="#FF5733",  fg="#641E16", highlightcolor="#CB4335", activebackground="#F4D03F")
        otherbutton = Button(bottomframe, text="CHEAT", relief=FLAT, width=30, height=h, font='arial 15', bg="#F5F5F5",
                             fg="#F5F5F5",  highlightcolor="#F5F5F5", activebackground="#F5F5F5")
        def shieldbutton_click(event):
            global yellowshield, redshield, blueshield
            shieldframe = Frame(root)
            shieldframe.place(x=screen_width*1/5, y=screen_height - 60, anchor=SW)
            yellowshield = Button(shieldframe, text="Kinetic shield (50☫)", relief=FLAT, width=20, height=1, font='arial 15',
                                  bg="#FF5733", fg="#641E16 ", highlightcolor="#CB4335", activebackground="#F4D03F")
            blueshield = Button(shieldframe, text="Energy shield (50☫)", relief=FLAT, width=20, height=1, font='arial 15',
                                  bg="#FF5733", fg="#641E16", highlightcolor="#CB4335", activebackground="#F4D03F")
            redshield = Button(shieldframe, text="Thermal shield (50☫)" , relief=FLAT, width=20, height=1, font='arial 15',
                                  bg="#FF5733", fg="#641E16", highlightcolor="#CB4335", activebackground="#F4D03F")
            yellowshield.pack(side=TOP)
            yellowshield.bind("<Button-1>", shield_l)
            blueshield.pack(side=TOP)
            blueshield.bind("<Button-1>", shield_e)            
            redshield.pack(side=TOP)
            redshield.bind("<Button-1>", shield_t)
            shieldbutton.bind("<Button-1>", shieldbutton_delete)

        def firebutton_click(event):
            fireframe = Frame(root)
            fireframe.place(x=screen_width * 2 / 5, y=screen_height - 60, anchor=SW)
            k_gun = Button(fireframe, text="Kinetic gun (50☫)", relief=FLAT, width=20, height=1, font='arial 15',
                                  bg="#FF5733", fg="#641E16", highlightcolor="#CB4335", activebackground="#F4D03F")
            t_gun = Button(fireframe, text="Thermal gun (50☫)", relief=FLAT, width=20, height=1, font='arial 15',
                                  bg="#FF5733", fg="#641E16", highlightcolor="#CB4335", activebackground="#F4D03F")
            e_gun = Button(fireframe, text="Plazma gun (50☫)", relief=FLAT, width=20, height=1, font='arial 15',
                                  bg="#FF5733", fg="#641E16", highlightcolor="#CB4335", activebackground="#F4D03F")                                  
            k_gun.pack(side=TOP)
            k_gun.bind("<Button-1>", k_gunup)
            t_gun.pack(side=TOP)
            t_gun.bind("<Button-1>", t_gunup)
            e_gun.pack(side=TOP)
            e_gun.bind("<Button-1>", e_gunup)


        def otherbutton_click(event):
            otherframe = Frame(root)
            otherframe.place(x=screen_width * 4 / 5, y=screen_height - 60, anchor=SW)
            mine = Button(otherframe, text="Mine", relief=FLAT, width=10, height=1, font='arial 15',
                                  bg="#FF5733", fg="#641E16", highlightcolor="#CB4335", activebackground="#F4D03F")
            mine.pack(side=TOP)
            mine.bind("<Button-1>", gold)
            
        def shieldbutton_delete(event):
            global yellowshield, redshield, blueshield
            yellowshield.pack_forget()
            redshield.pack_forget()
            blueshield.pack_forget()
            shieldbutton.bind("<Button-1>", shieldbutton_click)     
            
            
        shieldbutton.pack(side=LEFT, padx=2, pady=2)
        firebutton.pack(side=LEFT, padx=2, pady=2)
        powerbutton.pack(side=LEFT, padx=2, pady=2)
        powerbutton.bind("<Button-1>", cas_upgrade)
        otherbutton.pack(side=LEFT, padx=2, pady=2)
        otherbutton.bind("<Button-1>", shield)
        shieldbutton.bind("<Button-1>", shieldbutton_click)
        firebutton.bind("<Button-1>", firebutton_click)
        otherbutton.bind("<Button-1>", otherbutton_click)
        
def firetablet():
        global speed_scale
        upperframe = Frame(root)
        upperframe.place(x=2, y=2)

        up_btn = Button(upperframe, text="Up", width=9, height=4, font='arial 12', bg="#FF5733", fg="#641E16",
                        activebackground="#F4D03F")
        fire_btn = Button(upperframe, text="Fire", width=9, height=4, font='arial 12', bg="#FF5733", fg="#641E16",
                          activebackground="#F4D03F")
        down_btn = Button(upperframe, text="Down", width=9, height=4, font='arial 12', bg="#FF5733", fg="#641E16",
                          activebackground="#F4D03F")

        up_btn.pack(side=TOP)
        up_btn.bind("<Button-1>", up_handler)
        up_btn.bind("<ButtonRelease-1>", stop_motion)
        fire_btn.pack(side=TOP)
        fire_btn.bind("<Button-1>", shoot)
        down_btn.pack(side=TOP)
        down_btn.bind("<Button-1>", down_handler)
        down_btn.bind("<ButtonRelease-1>", stop_motion)
        down_btn.bind("<ButtonRelease-1>", stop_motion)
        speed_scale = Scale(upperframe, orient=HORIZONTAL, length=70,
                        from_=0, to=10)
        speed_scale.pack(side=TOP)
        speed_scale.bind("<Motion>", charge_inc)
        
shield = Protection()   
toolbar()
firetablet()

         


def draw_all():
    global balan
    mountain()
    enemy_castle.draw_castle()
    enemy_pushka.draw()    
    balan = canv.create_text(screen_width/2, 50, text= str(money) + '☫', font='Arial 50')
    C1.draw_castle()
    grass()
    for i in range(13):
        stone_ordinary(coordinate_x_stone_ordinary[i], random.randint(697, 760))
        stone_complicated(coordinate_x_stone_complicated[i], random.randint(697, 760))
    for i in range(5):
        cloud(coordinate_x_cloud[i], coordinate_y_cloud[i]) 





enemy_castle = Castle(gx+1200, gy, gr)

enemy_pushka = Gun(gx+1210, gy, 30, gun_number )
for _ in range (120):
    enemy_pushka.aim_up()

pushka = Gun(gx, gy, 30, gun_number )
C1 = Castle(gx, gy, gr)
enemy_shell = Shell(enemy_pushka.x_f, enemy_pushka.y_f, 30, -enemy_charge*40*math.cos(enemy_pushka.direction),  -enemy_charge*40*math.sin(enemy_pushka.direction), enemy_pushka.direction, enemy_shellcolor)
enemy_shell.destroy()
shell = Shell(pushka.x_f, pushka.y_f, 30, charge*40*math.cos(pushka.direction),  -charge*40*math.sin(pushka.direction), pushka.direction, shellcolor)
shell.destroy()
shield = None_protection(gx, gy)
draw_all()
hp = canv.create_text(1350, 650, text= str(enemy_castle.healthful) + '/' + str(enemy_castle.healthful), font='Arial 15', fill = '#003399')
shp = canv.create_text(150, 650, text= str(C1.healthful) + '/' + str(C1.healthful), font='Arial 15', fill = '#003399')
root.mainloop()
