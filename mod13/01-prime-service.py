from flask import Flask
from math import sqrt

app = Flask(__name__)

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    is_prime = True

    if number < 2:
        is_prime = False

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break

    response = {
        "Number": number,
        "isPrime": is_prime
    }

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
