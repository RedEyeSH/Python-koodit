array = []

while True:
    number = input("Enter a number: ")

    if number == "":
        break
    else:
        try:
            array.append(int(number))
        except ValueError:
            print("Please enter a number.")

array.sort()

print(f"Smallest number you have given: {array[0]}")
print(f"Largest number you have given: {array[-1]}")
