import re


def find_emails(input_string: str):
    # Regular expression for matching email addresses
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", input_string)


def extract_hashtags(input_string: str):
    # Use regex to find all hashtags
    return re.findall(r"#\w+", input_string)
