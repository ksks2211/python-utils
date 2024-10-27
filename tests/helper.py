import os
import random
from typing import TypeVar

from dotenv import load_dotenv

# .env 파일을 로드
load_dotenv()

T = TypeVar("T", int, float)


def get_env(key: str):
    return os.getenv(key)


def is_sorted(arr: list[T]) -> bool:
    size = len(arr)
    if size < 2:
        return True
    for i in range(1, size):
        if arr[i - 1] > arr[i]:
            return False
    return True


def random_integers(max: int, size: int):

    for _ in range(size):
        yield random.randint(0, max)
