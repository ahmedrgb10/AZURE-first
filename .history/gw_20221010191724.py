import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "5032e26898a6e1988442e3f44b39e2ff" #open('wmkey.txt','r').read()
CITY = "London"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()
print(response)

info = {}

info['lon'] = response['coord']['lon']
info['lat'] = response['coord']['lat']
info['wMain'] = response['weather'][0]['main']
info['wDes'] =  response['weather'][0]['description']
info['temp'] = response['main']['temp']
info['feels'] = response['main']['feels_like']
info['pressure'] = response['main']['pressure']
info['humidity'] = response['main']['humidity']
info['wSpeed'] = response['wind']['speed']
info['country'] = response['sys']['country']
info['sunrise'] = response['sys']['sunrise']
info['sunset'] = response['sys']['sunset']
#print(info)