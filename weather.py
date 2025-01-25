# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 18:59:12 2025

@author: singh
"""

import os
import requests
import sys

def fetch_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        print_weather(weather_data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        sys.exit(1)

def print_weather(data):
    city = data["name"]
    temp = data["main"]["temp"]
    weather_desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Description: {weather_desc}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    location = os.getenv("LOCATION")

    if not api_key or not location:
        print("Please provide API_KEY and LOCATION as environment variables.")
        sys.exit(1)

    fetch_weather(api_key, location)
