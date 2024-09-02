while True:
    inches = int(input("Enter inches: "))

    if inches < 0:
        break
    else:
        centimeters = inches * 2.54
        print(f"{inches} inches is {centimeters} centimeters.")