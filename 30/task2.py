"""
Home Work 30 - task 2
Dmytro Verovkin
robot_dreams
"""

import requests

city = input("Enter location: ")

CITY_API = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
city_res = requests.get(CITY_API)
if city_res.status_code == 200:
    city_res_data = city_res.json()
    latitude = city_res_data.get("results")[0]["latitude"]
    longitude = city_res_data.get("results")[0]["longitude"]

    # weather API
    WEATHER_FORECAST_API_URL = "https://api.open-meteo.com/v1/forecast"
    weather_api_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
    }
    weather_res = requests.get(WEATHER_FORECAST_API_URL, params=weather_api_params)
    if weather_res.status_code == 200:
        weather_res_data = weather_res.json().get("current_weather")
        print(f"The weather in {city} is - temperatute {weather_res_data['temperature']}°C and the wind speed is {weather_res_data['windspeed']} km/h")
    else:
        print("Error getting a weather")

else:   # city status API
    print("Error getting location coordinates, try later")
