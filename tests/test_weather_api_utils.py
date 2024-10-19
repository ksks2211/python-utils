from python_utils.api_utils.weather import (
    get_weather_by_city,
    get_weather_by_lat_and_lon,
)
from python_utils.date_utils import current_datetime
from python_utils.file_utils import file_exists
from python_utils.json_utils import save_dict_as_json
from tests.helper import get_env


def test_weather_api():
    owm_api_key = get_env("OWM_API_KEY")
    assert owm_api_key is not None

    city = "toronto"

    response = get_weather_by_city(city, owm_api_key)
    file = f"tmp/{city}-weather.json"

    if response is not None:
        save_dict_as_json(data=response, location=file)

    assert file_exists(file)


def test_weather_api_with_lat_lon():
    lat = 35.6895
    lon = 139.6917

    owm_api_key = get_env("OWM_API_KEY")
    assert owm_api_key is not None

    response = get_weather_by_lat_and_lon(lat, lon, owm_api_key)

    today = current_datetime()

    location = f"tmp/weather-{today}.json"

    if response is not None:
        save_dict_as_json(data=response, location=location)
    assert file_exists(location)
