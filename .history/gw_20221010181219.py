import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "5032e26898a6e1988442e3f44b39e2ff" #open('wmkey.txt','r').read()
CITY = "London"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()
print(response)

info = {'lon':'','lat':'','wMain':'','wDes':'','temp':'','feels':'','pressure':'','humidity':'','wspeed':'','country':'','sunrise':'',"sunset":''}

# info['lon'] = response['coord']['lon']
info['lat'] = response['coord']['lat']
info['wMain'] = response['weather']['main']
info['wDes'] = response['weather']['description']
info['temp'] = response['main']['temp']
info['feels'] = response['main']['feels_like']
info['pressure'] = response['main']['pressure']
info['humidity'] = response['main']['humidity']
info['wSpeed'] = response['wind']['speed']
info['country'] = response['sys']['country']
info['sunrise'] = response['sys']['sunrise']
info['sunset'] = response['sys']['sunset']
lon = response['coord']['lon']
print(lon)
print(info)

