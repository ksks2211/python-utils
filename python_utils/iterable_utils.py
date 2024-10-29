from collections import Counter
from typing import Any, Iterable


def count_element(elements: Iterable, element: Any):
    counter = Counter(elements)
    return counter[element]


def unique_elements(elements: Iterable):
    counter = Counter(elements)
    return tuple(counter.keys())
