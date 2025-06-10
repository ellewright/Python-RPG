import random

class Weapon:
    name = "Dagger"
    dmg_range = [8, 12]

    def use(self):
        return random.randint(self.dmg_range[0], self.dmg_range[1])