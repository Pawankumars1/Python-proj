import requests
import json

API_KEY = "85983651dc406e500ed14bb03fe5533a"

def get_weather(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        main_info = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        print(f"Weather in {city_name}: {main_info} ({description})")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print(f"Error: {data['message']}")

city_name = input("Enter the city name: ")
get_weather(city_name)

