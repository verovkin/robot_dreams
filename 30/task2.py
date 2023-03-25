"""
Home Work 30 - task 2
Dmytro Verovkin
robot_dreams
"""

import requests


class City:
    def __init__(self, __name = None):
        self.name = __name
        self.get_weather()

    def ask_city_name(self):
        self.name = input("Enter location: ")
        if self.name == 'exit':
            print("Good bye!")
            exit()

    def get_coordinates(self):

        while True:
            # ask city
            if self.name is None:
                self.ask_city_name()

            # request coordinates
            CITY_API = f"https://geocoding-api.open-meteo.com/v1/search?name={self.name}&count=1"
            city_res = requests.get(CITY_API)

            if city_res.status_code == 200:
                try:
                    city_res_data = city_res.json()
                    self.latitude = city_res_data.get("results")[0]["latitude"]
                    self.longitude = city_res_data.get("results")[0]["longitude"]
                except TypeError:
                    print(f"Cannot find {self.name}, please try once more! Or type 'exit' to quit.")
                    self.name = None
                else:
                    return True

            else:  # if coordinates API is not available - quit
                print("Error getting location coordinates, try later")
                exit()

    def get_weather(self):
        if self.get_coordinates():

            # weather API
            WEATHER_FORECAST_API_URL = "https://api.open-meteo.com/v1/forecast"
            weather_api_params = {
                "latitude": self.latitude,
                "longitude": self.longitude,
                "current_weather": True,
            }
            weather_res = requests.get(WEATHER_FORECAST_API_URL, params=weather_api_params)
            if weather_res.status_code == 200:
                weather_res_data = weather_res.json().get("current_weather")
                print(f"The weather in {self.name} is - temperatute {weather_res_data['temperature']}°C and the wind speed is {weather_res_data['windspeed']} km/h")
            else:
                print("Error getting a weather")
                exit()


city = City()
