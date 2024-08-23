import random

random_number = random.randint(1, 10)

while True:
    user_input = int(input("Enter a number: "))

    if user_input < random_number:
        print("Too low")
    elif user_input > random_number:
        print("Too high")
    else:
        print("Correct")
        break