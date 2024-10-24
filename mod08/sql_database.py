import mysql.connector

def airport_database():
    sql = f"SELECT name, municipality FROM airport LIMIT 10;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        if cursor.rowcount > 0:
            for row in result:
                print(row)

connection = mysql.connector.connect(
    host="localhost",
    port=3307, # Change your port to 3306 if necessary
    database="flight_game", # Enter your database name
    user="<username>", # Enter your username
    password="<password>", # Enter your password
    autocommit=True
)

if __name__ == "__main__":
    airport_database()