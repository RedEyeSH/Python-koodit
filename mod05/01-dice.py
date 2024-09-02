import random

total = 0
amountDice = int(input("How many dices you want to roll: "))

for i in range(amountDice):
    dice = random.randint(1,6)
    total += dice

print(f"You rolled {amountDice} times and got {total} in a total.")
