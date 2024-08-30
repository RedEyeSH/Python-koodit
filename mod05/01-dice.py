import random

x = 0

amountDice = int(input("How many dices you want to roll: "))

for i in range(0, amountDice):
    dice = random.randint(1,6)

    x += dice

print(f"You rolled {amountDice} times and got {x} in a total.")
