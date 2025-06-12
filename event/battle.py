def battle(char_a, char_b):
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