ICAO = {"EFHK": "Helsinki-Vantaan lentoasema"}

print("Welcome to the ICAO Airport Finder!")
print(f"Current airports in the system: {ICAO}\n")

while True:
    print("1 = Search, 2 = Add, 3 = Stop, 4 = Print all fields")
    number = input("Enter your choice (1, 2, 3 or 4): ")
    try:
        number = int(number)
        break
    except ValueError:
        print("\nPlease enter (1, 2, 3 or 4)!\n")
        continue

while number != 3:
    if number == 1:
        search = input("Enter the search term: ").upper()
        try:
            print("\nAirport name:", ICAO[search] + "\n")
        except KeyError:
            print("\nThe airport is not found!\n")
    elif number == 2:
        ICAO_code = input("Add ICAO code: ").upper()
        if ICAO_code in ICAO:
            print("\nThe airport already exists.\n")
        else:
            flight_name = input("Flight name: ")
            ICAO[ICAO_code] = flight_name
            print("\nA new airport has been added.\n")
    elif number == 4:
        print(f"\n{ICAO}\n")
    else:
        print("\nInvalid choice!\n")

    print("1 = Search, 2 = Add, 3 = Stop, 4 = Print all fields")
    number = int(input("Enter your choice (1, 2, 3 or 4): "))
