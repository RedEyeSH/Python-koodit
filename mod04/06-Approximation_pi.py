import random

number = 0
circle_point = 0

while True:
    N = input("Enter number of points to generate: ")
    try:
        N = int(N)
        if N <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer.")

while number < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        circle_point += 1

    number += 1

approximate_pi = 4 * (circle_point / N)

print("Approximation of pi:", approximate_pi)

