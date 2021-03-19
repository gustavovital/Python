"""
CodeHub - Weather info using python
Date: 19/03/2021
Author: Gustavo Vital
"""

import requests
import json

city = 'Delhi'
api_key = "API"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url)
x = response.json()
# print(x)

if x['cod'] != 401:
    print('City Name: ', x['name'])
    print('Weather: ', x['weather'])
    print('Weather: ', x['weather'][0]['main'])
    print('Temp: ', x['main']['temp'])
    print('Min Temp: ', x['main']['temp_min'])
    print('Max Temp: ', x['main']['temp_max'])
else:
    print('City not Found')