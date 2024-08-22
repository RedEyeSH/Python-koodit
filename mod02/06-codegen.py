import random

three_digit = ""
four_digit = ""

while len(three_digit) < 3:
    three_digit += str(random.randint(0, 9))

while len(four_digit) < 4:
    four_digit += str(random.randint(1, 6))

print("3-digit:", three_digit)
print("4-digit:", four_digit)