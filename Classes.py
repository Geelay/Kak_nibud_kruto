import math
import time 
from Classes import *
from tkinter import *
upg = 0
charge = 0
G = 9.8
gx= 280
gy= 160 
defe = 0
root = Tk()
root.overrideredirect(True) 
root.overrideredirect(False) 
root.attributes('-fullscreen', True)
GROUND_COLOR = 'white'
canv = Canvas(root, bg = GROUND_COLOR)
canv.pack(fill = BOTH, expand = 1)
gun_number = 0


class Protection():
    pass


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
        self.color = '#CCCCFF'
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
        self.color = '#FFDF84'
        self.health = 10

    def draw(self):
        canv.create_oval((self.x, self.y), (self.x + 2 * self.radius, self.y + 2 * self.radius),
                         fill='', outline=self.color, width=4)



class Castle():
    def __init__(self, x, y):
        self.health = 100
        self.x = x - 30
        self.y = y + 90
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



        
    def upgrade_1(self):
        self.health = 200
        self.x = 250
        self.y = 250
        self.size_x = 50
        self.size_y = 20
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

    def upgrade_2(self):
        self.health = 300
        self.x = 250
        self.y = 250
        self.size_x = 50
        self.size_y = 20
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

        


class Shell:
    def __init__(self, x, y, r, vx, vy, canvas, direction):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.direction = direction
        self.size = r
        self.delta_x = 0
        self.delta_y = 0
        
        self.canvas = canv
        self.oval = canv.create_oval (self.x + 2 * self.size, self.y + 0.2 * self.size, self.x + 2.6 * self.size, self.y+ 0.8 * self.size, fill='#32127A', outline='#32127A' )

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

        self.direction += self.size*math.pi/4400
        self.y_f -= math.cos(self.direction)
        self.x_f -= math.sin(self.direction)
        self.draw()
    def aim_down(self):

        self.direction -= self.size*math.pi/4400
        self.y_f += math.cos(self.direction)
        self.x_f += math.sin(self.direction)
        self.draw()
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
        pass

    def delete_self(self):
        self.canvas.delete(self.line1)
        self.canvas.delete(self.line2)
        self.canvas.delete(self.line3) 
