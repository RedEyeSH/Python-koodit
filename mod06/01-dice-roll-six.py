import random, time

def dice():
    while True:
        roll = random.randint(1,6)

        time.sleep(1)

        if roll == 6:
            print(f"Congratulations! You rolled a {roll}!")
            break
        else:
            print("Rolling a dice and got:", roll)

if __name__ == "__main__":
    dice()