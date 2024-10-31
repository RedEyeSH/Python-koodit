import requests

request = "https://api.chucknorris.io/jokes/random"
result = requests.get(request).json()
print(result["value"])
