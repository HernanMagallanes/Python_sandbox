# Fetching current weather data

import sys
import json
import requests

# Step 1: Get location from the command line argument

APPID = 'your_appId_here'

if len(sys.argv) < 2:
    print('Usage: gwtOpenWeather.py cityname, 2_letter_country_Code')
    sys.exit()

location = ' '.join(sys.argv[1:])

# Step 2: Download the JSON data

url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' % \
      (location, APPID)

response = requests.get(url)
response.raise_for_status()
print(response.text)

# Step 3: Load JSON data and print weather
weatherData = json.loads(response.text)

w = weatherData['list']

print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0][description])

print('\n')
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0][description])

print('\n')
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0][description])
