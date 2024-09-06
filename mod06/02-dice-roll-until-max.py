import random

def dice(number_sided_dice, maximum_value):
    while True:
        roll = random.randint(1,number_sided_dice)

        if roll == maximum_value:
            print(f"Congratulations! You rolled a {maximum_value}!")
            break
        else:
            print("Rolling a dice and got:", roll)

if __name__ == "__main__":
    while True:
        num_dice = input("Enter a number of sided dice: ")

        try:
            num_dice = int(num_dice)

            if num_dice <= 0:
                print("Please enter a number that is greater than 0!")
            else:
                break

        except ValueError:
            print("Please enter a valid number!")

    while True:
        maximum_val = input("Enter a maximum value: ")

        try:
            maximum_val = int(maximum_val)

            if num_dice >= maximum_val:
                break
            else:
                print(f"Maximum value cannot be greater than the number of sides: {num_dice}!")

        except ValueError:
            print("Please enter a valid number.")

    dice(num_dice, maximum_val)