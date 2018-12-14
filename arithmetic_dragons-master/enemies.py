# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

def check_simplicity(x):
    check = 0
    for i in range (1,x):
        if x % i == 0:
            check += 1
    if check < 2:
        return('да')
    else:
        return('нет')   
        
def check_number(x):
    check = 0
    list = []
    for i in range (1,x):
        if x % i == 0:
            check += 1
            list.append(i) 
    list.append(x)
    return(list)    

class Enemy(Attacker):
    pass

def generate_random_troll():
    RandomEnemyType = choice(enemy_super_types)
    enemy = RandomEnemyType()
    return enemy

def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy

def generate_troll_list(enemy_number):
    enemy_list = [generate_random_troll() for i in range(enemy_number)]
    return enemy_list

def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list

class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer
        
    def check_answer(self, answer):
        return answer == self.__answer

class CleverTroll(Troll):
    def __init__(self):
        self._healthfull = 100
        self._health = 100
        self._attack = 15
        self._experience = 50
        self._color = 'умный тролль'
        
    def question(self):
        x = randint(1,10)
        self.__quest = 'Угадай число'
        self.set_answer(x)
        return self.__quest
    
class TrollBrute(Troll):
    def __init__(self):
        self._healthfull = 100
        self._health = 100
        self._attack = 15
        self._experience = 50
        self._color = 'сильный тролль'
    
        
    def question(self):
        x = randint(1,100)
        self.__quest = 'Простое ли число ' + str(x) + '?'
        self.set_answer(check_simplicity(x))
        return self.__quest


class SuperCleverTroll(Troll):
    def __init__(self):
        self._healthfull = 100
        self._health = 100
        self._attack = 15
        self._experience = 50
        self._color = 'тролль из физтеха'
    
        
    def question(self):
        x = randint(1,100)
        self.__quest = 'Перечисли делители числа ' + str(x) + ' по порядку!'
        self.set_answer(check_number(x))
        return self.__quest

class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._healthfull = 200
        self._health = 200
        self._attack = 10
        self._experience = 20
        self._color = 'зелёный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest
    
class RedDragon(Dragon):
    def __init__(self):
        self._healthfull = 300        
        self._health = 300
        self._attack = 20
        self._experience = 30
        self._color = 'красный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest
    
class BlackDragon(Dragon):
    def __init__(self):
        self._healthfull = 500
        self._health = 500
        self._attack = 30
        self._experience = 50
        self._color = 'чёрный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest

#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.


enemy_types = [GreenDragon, RedDragon, BlackDragon]
enemy_super_types = [CleverTroll, SuperCleverTroll, TrollBrute]