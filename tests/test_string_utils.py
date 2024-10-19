import logging as logger

from python_utils.string_utils.extraction import extract_hashtags, find_emails
from python_utils.string_utils.transform import (
    normalize_spaces,
    remove_bracketed_text,
    remove_punctuation,
    to_snake_case,
)


def test_string_transform():
    #
    result = to_snake_case("CamelCaseExample")
    assert result == "camel_case_example"
    logger.info(f"After to_snake_case transform :  {result}")

    #
    result = remove_punctuation("Hello, World!")
    assert result == "Hello World"
    logger.info(f"After remove_punctuation transform : {result}")

    #
    result = normalize_spaces("Hello     World")
    assert result == "Hello World"
    logger.info(f"After normalize_spaces transform : {result}")


def test_string_transform2():
    result = remove_bracketed_text(
        """Tokyo, officially the Tokyo Metropolis (東京都, Tōkyō-to), is the capital of Japan and one of the most populous cities in the world, with a population of over 14 million residents as of 2023 and the second-most-populated capital in the world.[9] The Greater Tokyo Area, which includes Tokyo and parts of six neighboring prefectures, is the most-populous metropolitan area in the world, with 41 million residents as of 2024. Located at the head of Tokyo Bay, Tokyo is part of the Kantō region on the central coast of Honshu, Japan's largest island. Tokyo serves as Japan's economic center and the seat of both the Japanese government and the Emperor of Japan. The Tokyo Metropolitan Government administers Tokyo's central 23 special wards (which formerly made up Tokyo City), various commuter towns and suburbs in its western area, and two outlying island chains known as the Tokyo Islands. Despite most of the world recognizing Tokyo as a city, since 1943 its governing structure has been more akin to a prefecture, with an accompanying Governor and Assembly taking precedence over the smaller municipal governments which make up the metropolis. Notable special wards in Tokyo include Chiyoda, the site of the National Diet Building and the Tokyo Imperial Palace; Shinjuku, the city's administrative center; and Shibuya, a commercial, cultural, and business hub in the city."""
    )
    logger.info(f"After remove_bracketed_text transform : {result}")
