from model.weapon import Weapon
import random

class Monster:
    level = 1
    name = "Ghost"
    health = random.randint(1, 25)
    weapon = Weapon

    def attack(self):
        return self.weapon.use(self.weapon)