import aiohttp

URL = "https://api.openweathermap.org/data/2.5/weather"


async def get_weather_by_city(city: str, OWN_API_KEY: str):
    params = {"q": city, "appid": OWN_API_KEY, "units": "metric"}
    async with aiohttp.ClientSession() as session:
        async with session.get(URL, params=params) as response:
            return await response.json()
