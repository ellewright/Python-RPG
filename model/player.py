from model.weapon import Weapon
import random

class Player:
    name: str
    health = 25
    weapon = Weapon

    def __init__(self, name):
        self.name = name

    def attack(self):
        return self.weapon.use(self.weapon)