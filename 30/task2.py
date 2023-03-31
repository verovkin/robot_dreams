"""
Home Work 30 - task 2
Dmytro Verovkin
robot_dreams
"""

import requests


class City:
    def __init__(self, name):
        self.name = name
        self.set_coordinates()

    def set_coordinates(self):
        self.lat, self.lon = WeatherService.get_coordinates(self.name)

    def print_weather(self):
        weather_data = WeatherService.get_current_weather(self.lat, self.lon)
        if weather_data:
            print(f"The weather in {self.name} is - temperatute {weather_data['temperature']}°C and the wind speed is {weather_data['windspeed']} km/h")
        else:
            print(f"There is no weather for {self.name} city.")


class WeatherService:
    @classmethod
    def get_coordinates(self, name):
        # request coordinates
        CITY_API = f"https://geocoding-api.open-meteo.com/v1/search?name={name}&count=1"

        try:
            city_res = requests.get(CITY_API)
        except requests.exceptions.ConnectionError as e:
            raise ValueError("Check your internet connection")

        if city_res.status_code == 200:
            try:
                city_res_data = city_res.json()
                lat = city_res_data.get("results")[0]["latitude"]
                lon = city_res_data.get("results")[0]["longitude"]
            except TypeError:
                raise ValueError('No such city')

            return lat, lon

        else:  # if coordinates API is not available - quit
            raise ValueError("Geo coordinate service is not working")

    @classmethod
    def get_current_weather(self, lat, lon):
        # weather API
        WEATHER_FORECAST_API_URL = "https://api.open-meteo.com/v1/forecast"
        weather_api_params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True,
        }

        try:
            weather_res = requests.get(WEATHER_FORECAST_API_URL, params=weather_api_params)
        except requests.exceptions.ConnectionError as e:
            raise ValueError("Check your internet connection")

        if weather_res.status_code == 200:
            return weather_res.json().get("current_weather")
        else:
            raise ValueError("Weather service is not working")


city_name = input("Enter city: ")
try:
    city = City(city_name)
except ValueError as e:
    print(e)
else:
    city.print_weather()
