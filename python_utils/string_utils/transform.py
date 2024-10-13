import re


def to_snake_case(input_string: str):
    # Replace capital letters with an underscore followed by lowercase
    return re.sub(r"(?<!^)(?=[A-Z])", "_", input_string).lower()


def remove_punctuation(input_string: str):
    # Use regex to replace punctuation with an empty string
    return re.sub(r"[^\w\s]", "", input_string)


def remove_bracketed_text(text: str) -> str:
    # [ 대괄호로 시작해서 숫자나 문자들로 구성된 문자열로 끝나는 부분 ], Lazy
    return re.sub(r"\[.*?\]", "", text)


def normalize_spaces(input_string: str):
    # Replace multiple spaces with a single space
    return re.sub(r"\s+", " ", input_string).strip()
