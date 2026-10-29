import random

def cast_die():
    die_roll = random.randint(1, 6)
    return f"You rolled a {die_roll}!"

while True:
    dice_roll = input("Roll the dice? (y/n): ")

    if dice_roll.lower() == 'y' or dice_roll.lower() == 'yes':
        print(cast_die())
    elif dice_roll.lower() == 'n' or dice_roll.lower() == 'no':
        print("Okay, maybe next time!")
        break
    else :
        print("Invalid input. Please enter 'y' or 'n'.")