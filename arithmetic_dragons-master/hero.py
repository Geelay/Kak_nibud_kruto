# coding: utf-8
# license: GPLv3
from gameunit import *
class Hero(Attacker):
    def __init__(self, name):
        self._health = 100
        self._healthfull = 100
        self._attack = 50
        self._experience = 0
        self.name = name
        self.item = None
    def attack(self, target):
        target._health -= self._attack
        print(target._color, target._health, '/', target._healthfull, 'HP')
        
    def item_claim(self, target):
        self.item = target._item

    
    def exp_gain(self, target):
        self._experience += target._experience
            
    def is_lvl_up(self):
        if  self._experience > 99:
            return(True)
    
    def lvl_up(self):
        self._attack += 10
        self._health = 100
        
    def exp_down(self):
        self._experience = 0

#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""
