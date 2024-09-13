import mysql.connector

def airport_type(area_code):
    area_code.upper()

    small_airport_count = 0
    heliport_count = 0
    medium_airport_count = 0
    closed_port_count = 0

    sql = f"SELECT type FROM airport WHERE iso_country = '{area_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        if cursor.rowcount > 0:
            for row in result:
                if row[0] == "small_airport":
                    small_airport_count += 1
                elif row[0] == "heliport":
                    heliport_count += 1
                elif row[0] == "medium_airport":
                    medium_airport_count += 1
                else:
                    closed_port_count += 1

    return small_airport_count, heliport_count, medium_airport_count, closed_port_count

connection = mysql.connector.connect(
    host="localhost",
    port=3307, # Change your port to 3306 if necessary
    database="flight_game", # Enter your database name
    user="<username>", # Enter your username
    password="<password>", # Enter your password
    autocommit=True
)

if __name__ == "__main__":
    area_code = input("Enter area code: ")
    ap, hp, af, cp = airport_type(area_code)

    print(f"Number of small airports: {ap}")
    print(f"Number of heliports: {hp}")
    print(f"Number of medium airports: {af}")
    print(f"Number of closed ports: {cp}")

