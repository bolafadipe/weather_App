import requests
#import datetime
import json
from pprint import pprint
from tkinter.messagebox import showerror
from dotenv import load_dotenv
import os


load_dotenv()

def get_weather(city):

    #def __init__(self, city):
    api_key = os.getenv('API_KEY')

    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    #def get_weather(self):
    
    res = requests.get(url)
    data = res.json()
    
        
        
        
    if data["cod"] == "404":
        showerror('Error','City Not Found !')
        
    else:
        weather = data["main"]
        location = data['name'] + ", " + data['sys']['country']
        current_temp = weather["temp"] - 274
        current_temp = round(current_temp,0)
        current_temp = str(current_temp) + ' ' + '°C'
        feels_like_temp = weather['feels_like'] - 274
        feels_like_temp = str(round(feels_like_temp,0)) + ' ' + '°C'
        current_pressure = round(weather["pressure"] * 0.0009869233, 2)
        current_pressure = str(current_pressure) + ' ' + 'atm'
            #self.current_pressure = str(self.current_pressure
            #print(self.current_pressure)
        current_humidity = str(weather["humidity"]) + '%'
            #print(self.current_humidity)
        # current_pressure *= 0.0009869233
        # current_humidity = y["humidity"]
        description = data["weather"]
        weather_icon = data['weather'][0]['icon']
            
        weather_description = description[0]["description"]

        #city = data['name']
        #country = data['sys']['country']
        wind_speed = data['wind']['speed']
        
        all_info = [location, current_temp, feels_like_temp, weather_icon, weather_description, current_pressure, current_humidity, wind_speed]
        #print(data)
        return all_info
            #print(self.weather_description)
        # degree_sign = u"\N{DEGREE SIGN}"
        # temperature = "{:.0f}".format(current_temperature) + degree_sign + "C"
        # pressure = "{:.0f}".format(current_pressure) + " atm"
        # humidity = str(current_humidity) + "%"
        # details = weather_description

        

if __name__ == '__main__':
    get_weather()
    #city_weather = get_weather('London')
    #print(city_weather)
    #weather.get_weather()
