array = []

while True:
    number = input("Enter a number: ")

    if number == "":
        break
    else:
        try:
            array.append(int(number))
        except ValueError:
            print("Please enter a number!")

array.sort(reverse=True)

if len(array) > 4:
    for i in range(len(array)):
        print(array[i])