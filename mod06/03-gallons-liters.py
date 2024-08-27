def convert():
    while True:
        gallons = input("Gallons: ")
        try:
            gallons = int(gallons)
            if gallons < 0:
                break
            else:
                print(f"{gallons} gallons is {gallons * 3.785} liters.")
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    convert()
