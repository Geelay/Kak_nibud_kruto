from gameunit import *

class Hero(Attacker):
    def __init__(self, name):
        self._health = 100
        self._attack = 50
        self._name = name
        self._experience = 0

    def attack(self, target):
        target._health -= self._attack
        self._experience +=5

        
