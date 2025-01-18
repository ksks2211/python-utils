import pytest

from python_utils.api_utils.aio_weather import get_weather_by_city
from python_utils.file_utils import file_exists
from python_utils.json_utils import save_dict_as_json
from tests.helper import get_env


@pytest.mark.asyncio
async def test_weather_api():

    owm_api_key = get_env("OWM_API_KEY")
    assert owm_api_key is not None
    city = "madrid"

    response = await get_weather_by_city(city, owm_api_key)
    file = f"tmp/{city}-weather.json"
    if response is not None:
        save_dict_as_json(data=response, location=file)

    assert file_exists(file)
