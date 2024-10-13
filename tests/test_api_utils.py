from python_utils.api_utils.weather import (
    get_weather_by_city,
    get_weather_by_lat_and_lon,
)
from python_utils.file_utils import file_exists
from python_utils.json_utils import save_dict_as_json
from tests.helper import get_env


def test_weather_api():
    owm_api_key = get_env("OWM_API_KEY")
    assert owm_api_key is not None

    city = "tokyo"

    response = get_weather_by_city(city, owm_api_key)
    file = "tmp/tokyo-weather.json"

    if response is not None:
        save_dict_as_json(data=response, location="tmp/tokyo-weather.json")

    assert file_exists(file)
