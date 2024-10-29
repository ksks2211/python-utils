import logging as logger

from python_utils.algo_utils.two_pointer import find_interval_sum, merge
from tests.helper import is_sorted, random_integers


def test_merge():

    sorted_arr1 = sorted(list(random_integers(2000, 100)))
    sorted_arr2 = sorted(list(random_integers(2000, 100)))

    sorted_result = merge(sorted_arr1, sorted_arr2)

    assert is_sorted(sorted_result)


def test_find_interval_sum():

    arr = [1, 2, 3, 2, 5]

    target = 5

    for start, end in find_interval_sum(arr, target):
        assert sum(arr[start:end]) == target

    interval_sum_count = sum(True for _ in find_interval_sum(arr, target))

    assert interval_sum_count == 3
