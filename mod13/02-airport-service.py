import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

def database_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        database="<database>",
        user="<user>",
        password="<password>",
        autocommit=True
    )

@app.route('/airport/<string:icao>', methods=['GET'])
def get_airport_data(icao):
    icao = icao.upper()
    sql = f"SELECT name, municipality FROM airport WHERE gps_code = %s"
    conn = database_connection()
    cursor = conn.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    if result:
        response = {
            "ICAO": icao,
            "Name": result[0],
            "Location": result[1]
        }

        return jsonify(response)
    else:
        response = {
            "Message": "Airport not found",
            "status": 404
        }

        return jsonify(response)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)