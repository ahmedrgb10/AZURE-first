import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "5032e26898a6e1988442e3f44b39e2ff" #open('wmkey.txt','r').read()
CITY = "London"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url)
print(response)