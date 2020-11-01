"""
Simple implementation of the OpenWeatherMaps (OWM) API
"""

import json
import requests
from requests.exceptions import HTTPError

class Owm:
    def __init__(self, city, api_key):
        self.req_uri='http://api.openweathermap.org/data/2.5/forecast?q='+city+',hu&APPID='+api_key           

    def get_weather(self):
        try:
            response = requests.get(self.req_uri)
        except HTTPError as http_err:
            print('HTTP problem:' + http_err)
        except Exception as err:
            print("An error occured:")
            print(err)
        else:
           return response

if __name__ == '__main__':
    weather = Owm('demecser', '8896cf78c022c0ec61fac18730502f42')
    weather_json = weather.get_weather().json()
    print(weather_json)

