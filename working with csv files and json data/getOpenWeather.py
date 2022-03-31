# Fetching current weather data

import sys
import json
import requests

import os
from dotenv import load_dotenv

# Step 1: Get location from the command line argument

load_dotenv()
APPID = os.getenv('APY_KEY')

if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_Code')
    sys.exit()

country = sys.argv[-1]

if len(country) > 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_Code')
    sys.exit()

# format city name
# 'buenos aires' -> 'buenos%20aires'

raw_city = sys.argv[1:-1]

city = ''

for index, word in enumerate(raw_city):
    if index == 0:
        city += word
        continue

    city += f'%20{word}'

# Step 2: Download the JSON data

# with city str
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}{country}&appid={APPID}&units=metric'

response = requests.get(url)
response.raise_for_status()

# raw data
# print(response.text)

# Step 3: Load JSON data and print weather

weatherData = json.loads(response.text)

print(f"\nCurrent weather in {weatherData['name']}, {weatherData['sys']['country']} \n")

print(f"{weatherData['weather'][0]['main']} - {weatherData['weather'][0]['description']} \n")

print(f"Temperature: {weatherData['main']['temp']} ºC \n")

print(f"feels likes: {weatherData['main']['feels_like']} ºC \n")

print(f"Pressure: {weatherData['main']['pressure']} hPa \n")

print(f"Humidity: {weatherData['main']['humidity']} % \n")

print(f"wind speed: {weatherData['wind']['speed']} meter/sec \n")
