from model.player import Player

# TODO: Create monster class
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
    

if __name__ == "__main__":
    main()