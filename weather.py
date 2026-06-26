import requests
from datetime import datetime
from config import API_KEY


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    weather = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind": data["wind"]["speed"],
        "visibility": data["visibility"],
        "condition": data["weather"][0]["description"].title(),
        "sunrise": datetime.fromtimestamp(
            data["sys"]["sunrise"]
        ).strftime("%I:%M %p"),
        "sunset": datetime.fromtimestamp(
            data["sys"]["sunset"]
        ).strftime("%I:%M %p"),
    }

    return weather
