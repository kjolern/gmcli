import random
import main


def roll_dice(num_dice, num_sides):
    #Rolls a specified number of dice with a given number of sides.
    results = []
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        results.append(roll)
    return results

def roller():
    #Main function to interact with the user and roll dice.
    while True:
        try:
            dice_string = input("Enter dice roll or type exit(e.g., 2d6, 1d20, 3d8+2): ").lower()

            if dice_string == 'exit':
                main.main()

            if '+' in dice_string:
                base, modifier_str = dice_string.split('+')
                modifier = int(modifier_str)
            elif '-' in dice_string:
                base, modifier_str = dice_string.split('-')
                modifier = -int(modifier_str)
            else:
                base = dice_string
                modifier = 0

            if 'd' in base:
                num_dice_str, num_sides_str = base.split('d')
                num_dice = int(num_dice_str)
                num_sides = int(num_sides_str)
                results = roll_dice(num_dice, num_sides)

            else:
                print("Invalid dice format. Please use the format 'XdY+Z' or 'exit'.")
                continue

            total = sum(results) + modifier
            print(f"Rolled: {results}")
            print(f"Total (including modifier {modifier}): {total}")

        except ValueError:
            print("Invalid input. Please enter numbers only or 'exit'.")
        except Exception as e:
            print(f"An error occurred: {e}")
