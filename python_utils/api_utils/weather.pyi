from typing import TypedDict

class Coord(TypedDict):
    lon: float
    lat: float

class Weather(TypedDict):
    id: int
    main: str
    description: str
    icon: str

class Main(TypedDict):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int

class Clouds(TypedDict):
    all: int

class Wind(TypedDict):
    speed: float
    deg: int

class Sys(TypedDict):
    type: int
    id: int
    country: str
    sunrise: str
    sunset: str

class WeatherResponse(TypedDict):
    coord: Coord
    weather: list[Weather]
    base: str
    main: Main
    visibility: int
    wind: Wind
    clouds: Clouds
    dt: int
    sys: Sys
    timezone: float
    id: int
    name: str
    cod: int

def get_weather_by_lat_and_lon(
    lat: float, lon: float, api_key: str
) -> WeatherResponse: ...
def get_weather_by_city(city: str, api_key: str) -> WeatherResponse: ...
