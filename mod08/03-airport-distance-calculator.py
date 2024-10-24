import mysql.connector
from geopy import distance

def distance_airport(icao):
    coordinate_list = []
    location_list = []

    for i in range(len(icao)):
        sql = f"SELECT latitude_deg, longitude_deg, name FROM airport WHERE gps_code = '{icao[i]}'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        if result:
            if cursor.rowcount > 0:
                for row in result:
                    coordinate_list.append((row[0], row[1])) # Latitude, longitude
                    location_list.append(row[-1]) # airport name

    return coordinate_list, location_list

connection = mysql.connector.connect(
    host="localhost",
    port=3307, # Change your port to 3306 if necessary
    database="flight_game", # Enter your database name
    user="<username>", # Enter your username
    password="<password>", # Enter your password
    autocommit=True
)

if __name__ == "__main__":
    icao_list = []

    count = 1

    while len(icao_list) < 2:
        icao_code = input(f"Enter ICAO code for airport {count}: ").upper()

        # Checks if ICAO code exists
        sql = f"SELECT latitude_deg, longitude_deg, name FROM airport WHERE gps_code = '{icao_code}'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        if result:
            count += 1
            icao_list.append(icao_code)
        else:
            print("\nPlease enter a valid ICAO code.\n")

    cal_distance, airport_location = distance_airport(icao_list)

    location_deg1 = cal_distance[0]
    location_deg2 = cal_distance[1]

    dist = distance.distance(location_deg1, location_deg2).km

    print(f"\n{airport_location[0]} coordinate: {location_deg1}")
    print(f"{airport_location[1]} coordinate: {location_deg2}")
    print(f"Distance between {airport_location[0]} and {airport_location[1]}: {dist:.2f} km.")
