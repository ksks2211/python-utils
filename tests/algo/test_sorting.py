import logging as logger

from python_utils.algo_utils.sorters import bubble_sort, insertion_sort, selection_sort
from tests.helper import is_sorted, random_integers


def test_sorters():
    arr = list(random_integers(20000, 5000))

    sorted_arr = bubble_sort(arr[:])
    assert is_sorted(sorted_arr)

    sorted_arr = insertion_sort(arr[:])
    assert is_sorted(sorted_arr)

    sorted_arr = selection_sort(arr[:])
    assert is_sorted(sorted_arr)
