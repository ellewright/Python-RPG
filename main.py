from event.create_character import create_character
from event.create_monster import create_monster
from event.battle import battle

def main():
    print("Welcome to the Python RPG!")

    # Create character
    player = create_character()

    # Create monster
    monster = create_monster()

    # First fight
    battle(player, monster)

if __name__ == "__main__":
    main()