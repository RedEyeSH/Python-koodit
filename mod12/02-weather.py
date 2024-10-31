import requests

API_KEY = "<API_KEY>"
KELVIN_TO_CELSIUS = 273.15

city = input("Enter a city name: ")

coordinate_request = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}"
coordinate_response = requests.get(coordinate_request)

json_format = coordinate_response.json()

lat = json_format[0]["lat"]
lon = json_format[0]["lon"]

weather_request = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
weather_response = requests.get(weather_request)

json_format_weather = weather_response.json()
main = json_format_weather["main"]
weather = json_format_weather["weather"][0]

temp_max = main["temp_max"] - KELVIN_TO_CELSIUS
description = weather["description"]

print(f"Weather condition: {description}")
print(f"Temperature: {round(temp_max)}°C")
