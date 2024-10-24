import mysql.connector
from geopy import distance
from random import randint

# =====================================================
# For example
def country_query(country):
    airport_country_list = []
    sql = f"SELECT airport.name FROM country INNER JOIN airport ON country.iso_country = airport.iso_country WHERE country.name = '{country}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        for row in result:
            airport_country_list.append(row[0])

        return airport_country_list

def city_query(country, city, amount_airports):
    airport_city_list = []
    sql = f"SELECT airport.name FROM airport INNER JOIN country ON airport.iso_country = country.iso_country WHERE country.name = '{country}' AND airport.municipality = '{city}' ORDER BY airport.name DESC LIMIT {amount_airports}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        for row in result:
            airport_city_list.append(row[0])
        return airport_city_list

def airport_information(country, city, icao):
    sql = f"SELECT airport.name FROM airport INNER JOIN country ON airport.iso_country = country.iso_country WHERE country.name = '{country}' AND airport.municipality = '{city}' AND airport.gps_code = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        for row in result:
            return row[0]
# =====================================================

# =====================================================
# Main tasks
def get_airports_by_country(country):
    airport_list = []
    sql = f"SELECT airport.name FROM airport INNER JOIN country ON airport.iso_country = country.iso_country WHERE country.name = '{country}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        for row in result:
            airport_list.append(row[0])

        return airport_list

def get_airports_by_city(city):
    city_list = []
    sql = f"SELECT airport.name FROM airport INNER JOIN city ON airport.iso_country = city.iso_country WHERE city.name = '{city}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        for row in result:
            city_list.append(row[0])

        return city_list

# A database connection
connection = mysql.connector.connect(
    host="localhost",
    port=3307, # Change your port to 3306 if necessary
    database="flight_game", # Enter your database name
    user="root", # Enter your username
    password="Metropolia05", # Enter your password
    autocommit=True
)

# ======================================================
# For example
print("""
FindYourWay is a fun travel planning game where you explore the world by choosing flights between major airports. 
Pick your starting country and destination, get the distance, and see how much CO2 your flight will use. 
Confirm if you're ready to travel knowing the environmental impact.

Features:
- Choose Destinations: Select from the top 10 largest cities and airports in each country.
- CO2 Awareness: See how much CO2 your flight produces and make eco-conscious decisions.
- Random Destination Generator: Get a surprise destination for a spontaneous adventure.

Ready to travel? Play FindYourWay and discover your next journey!
""")


program = input("(Y/N): ").upper()

if program == "Y": # Used for shortcut for the main tasks
    while True:
        country_input = input("Enter a country name: ").capitalize()
        country_list = country_query(country_input)
        if country_list:
            print(f"All airports found in the {country_input}:\n")
            for countries in country_list:
                print(f"    {countries}") ## Suggested edit print(f"All airports in {country_input}: \n")
            ## Add for loop: for country in country_list print(f"\t{country}")
            ## After for loop print("\n")
            break
        else:
            print("\nInvalid country, try again.\n")

    while True:
        city_input = input(f"\nEnter {country_input}'s city name: ").capitalize()
        city_list = city_query(country_input, city_input)
        if city_list:
            amount_of_airports = 0
            for i in range(len(city_list)):
                amount_of_airports += 1
            print(f"Amount of airports in the ({city_input}) were found in a total {amount_of_airports}") # This is just for testing
            airport_by_size = input(f"Enter any amount of airports ({amount_of_airports}): ") # This is just for testing
            print(f"Airports found in the city: {city_input}\n")
            # Selecting top airports by user--
            # And then
            for cities in city_list:
                print(f"    {cities}")
            print("")
            break
        else:
            print(f"\nInvalid city, please enter a city in {country_input} that has an airport.\n")

    while True:
        icao_input = input("Enter an icao code: ").upper()
        airport_name = airport_information(country_input, city_input, icao_input)
        if airport_name:
            print(f"Airport: {airport_name}\n")
            break
        else:
            print("\nInvalid icao code, please try again.\n")
else:
    print("Continuing...")
# =====================================================

# =====================================================
# Main tasks
while True:
    print("1 = Search country, 2 = Search city, 3 = Search an airport by ICAO , 4 = Random Destination Generator 5 = Stop the program: ")
    options = input("Enter your choice (1, 2, 3, 4 or 5): ")

    if options == "1":
        search_country = input("Enter a country name: ").capitalize()
        airports = get_airports_by_country(search_country)
        print(airports)
    elif options == "2":
        search_city = input("Enter a city name: ").capitalize()
        cities = get_airports_by_city(search_city)
        print(cities)
    elif options == "3":
        pass
    elif options == "5":
        print("Stopping...")
        break
    else:
        print("Invalid choice, please enter (1, 2, 3, 4 or 5)")



