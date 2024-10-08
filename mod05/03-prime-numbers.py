import math

number = int(input("Enter a number: "))

square_root = math.sqrt(number)

is_prime = None

if number < 2:
    print(number, "is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(square_root) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")