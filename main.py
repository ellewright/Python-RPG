from model.player import Player
from model.monster import Monster

# TODO: Create weapon class
def main():
    player_confirmed = False
    player_created = False

    print("Welcome to the Python RPG!")

    while not player_created and not player_confirmed:
        entered_name = input("To begin, what is your name? ")
        confirmed = input(f"Your name is {entered_name}? (y/n) ").lower()

        if confirmed == "y":
            player_confirmed = True
            player = Player(entered_name)
            player_created = True
        elif confirmed == "n":
            print("Whoops, sorry!")
            continue
        else:
            print("Please answer yes or no (y/n).")
            continue

    print(f"Welcome, {player.name}!")

    # First fight
    monster = Monster()

    print(f"Oh no, you have stumbled across a {monster.name}! It has {monster.health} health!")

    fight(player, monster)
    
def fight(char_a, char_b):
    fight_over = False

    while not fight_over:
        char_a_attack = char_a.attack()
        char_b_attack = char_b.attack()

        char_b.health -= char_a_attack
        char_a.health -= char_b_attack

        print(f"{char_a.name} strikes {char_b.name} with its {char_a.weapon.name} for {char_a_attack} points.")
        print(f"{char_b.name} strikes {char_a.name} with its {char_b.weapon.name} for {char_b_attack} points.")

        print(f"{char_a.name}'s health is now {char_a.health}.")
        print(f"{char_b.name}'s health is now {char_b.health}.")

        if char_a.health <= 0:
            print(f"{char_a.name} died!")
            fight_over = True
        elif char_b.health <= 0:
            print(f"{char_b.name} died!")
            fight_over = True

if __name__ == "__main__":
    main()