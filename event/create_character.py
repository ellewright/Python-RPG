import random
from model.path import Path
from model.player import Player

def create_character():
    player_confirmed = False
    player_created = False
    
    while not player_created and not player_confirmed:
        entered_name = input("To begin, what is your name? ")
        confirmed = input(f"Your name is {entered_name}? (y/n) ").lower()

        if confirmed == "y":
            paths = [Path.WARRIOR, Path.DRUID, Path.THIEF, Path.MAGE]

            player_confirmed = True
            player = Player(entered_name, paths[random.randint(0, len(paths) - 1)])
            player_created = True
        elif confirmed == "n":
            print("Whoops, sorry!")
            continue
        else:
            print("Please answer yes or no (y/n).")
            continue

    print(f"Welcome, {player.name}!")
    print(f"You are a level {player.level} {player.path}.")

    return player