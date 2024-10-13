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
    result = remove_bracketed_text("Hello[1] World")
    assert result == "Hello World"
    logger.info(f"After remove_bracketed_text transform : {result}")
