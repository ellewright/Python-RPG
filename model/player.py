from model.path import Path
from model.weapon import Weapon

class Player:
    level = 1
    xp = 0
    path = Path
    name: str
    health = 25
    weapon = Weapon

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def attack(self):
        return self.weapon.use(self.weapon)