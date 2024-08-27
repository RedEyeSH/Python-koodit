number = int(input("Enter a number: "))

prime_numbers = [2, 3]

if number % 2 == 0:
    print("Prime number")
elif number % 3 == 0:
    print("Prime number")
elif number % 5 == 0:
    print("Prime number")

for i in range(len(prime_numbers)):
    if number % prime_numbers[i] == 0:
        print("Prime number")
    else:
        print("Not a prime number")

