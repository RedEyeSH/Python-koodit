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

result_array = []

if len(array) > 5:
    for i in range(5):
        result_array.append(array[i])
    print(f"Five highest numbers: {result_array}")
else:
    # This is for if the user enters under 5 numbers.
    for i in range(len(array)):
        result_array.append(array[i])
    print(f"{len(result_array)} Greatest numbers: {result_array}")

