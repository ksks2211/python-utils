import requests

URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather_by_lat_and_lon(lat: float, lon: float, OWN_API_KEY: str):
    params = {"lat": lat, "lon": lon, "appid": OWN_API_KEY}
    response = requests.get(URL, params=params)
    if response.status_code != 200:
        response.raise_for_status()
    return response.json()


def get_weather_by_city(city, OWN_API_KEY: str):
    params = {"q": city, "appid": OWN_API_KEY, "units": "metric"}
    response = requests.get(URL, params=params)
    if response.status_code != 200:
        response.raise_for_status()
    return response.json()
