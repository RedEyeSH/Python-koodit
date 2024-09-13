import mysql.connector

def airport(icao):
    icao.upper()

    sql = f"SELECT name, municipality FROM airport WHERE gps_code='{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        if cursor.rowcount > 0:
            for row in result:
                return row[0], row[1]
    else:
        return None, None

connection = mysql.connector.connect(
    host="localhost",
    port=3307, # Change your port to 3306 if necessary
    database="flight_game", # Enter your database name
    user="<username>", # Enter your username
    password="<password>", # Enter your password
    autocommit=True
)

if __name__ == "__main__":
    ICAO_code = input("Enter ICAO code: ")
    name, town = airport(ICAO_code)

    if (name and town) and ICAO_code != "":
        print(f"The airport name: {name}")
        print(f"It's located in the town of: {town}")
    else:
        print("No airport found.")