import requests

key = 'd73af82268fa4a64a3c200007231402'
city = 'Riga'
url = 'http://api.weatherapi.com/v1/current.json?key='+key+'&q='+city+'&aqi=no'

response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_c')
description = weather_json.get('current').get('condition').get('text')

print("Today's weather in", city, "is", description, "and", temp, "degrees")