import logging as logger
from itertools import permutations

from python_utils.algo_utils.permutations import (
    next_permutation,
    permutations_with_duplication,
    prev_permutation,
)


def test_permutations():

    original = [1, 2, 3, 4, 5]
    arr = original[:]

    next_permutation(arr)
    logger.info(arr)
    prev_permutation(arr)
    logger.info(arr)

    assert arr == original

    assert not prev_permutation(arr)


def test_permutations_with_dup():
    duplicated_items = ["A", "A", "B", "B", "C"]

    for items in permutations_with_duplication(duplicated_items, 3):
        logger.info(list(items))

    noc = sum(True for _ in permutations_with_duplication(duplicated_items, 3))
    assert noc == len(set(permutations(duplicated_items, 3)))

    logger.info(f"Number of cases : {noc}")
