import logging as logger

from python_utils.algo_utils.permutations import next_permutation, prev_permutation


def test_permutations():

    original = [1, 2, 3, 4, 5]
    arr = original[:]

    next_permutation(arr)
    logger.info(arr)
    prev_permutation(arr)
    logger.info(arr)

    assert arr == original

    assert not prev_permutation(arr)
