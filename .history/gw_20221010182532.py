import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "5032e26898a6e1988442e3f44b39e2ff" #open('wmkey.txt','r').read()
CITY = "London"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()
print(response)

info = {}
info['a']=0

info['lon'] = str(response['coord']['lon'])
info['lat'] = str(response['coord']['lat'])
info['wMain'] = str(response['weather']['main'])
info['wDes'] = str(response['weather']['description'])
info['temp'] = str(response['main']['temp'])
info['feels'] = str(response['main']['feels_like'])
info['pressure'] = str(response['main']['pressure'])
info['humidity'] = str(response['main']['humidity'])
info['wSpeed'] = str(response['wind']['speed'])
info['country'] = str(response['sys']['country'])
info['sunrise'] = str(response['sys']['sunrise'])
info['sunset'] = str(response['sys']['sunset'])

print(info)

