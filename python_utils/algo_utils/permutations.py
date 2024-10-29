from collections import Counter
from itertools import product
from typing import Any, List, TypeVar

T = TypeVar("T", int, float)


def next_permutation(arr: list[T]):

    # size of array
    n = len(arr)

    # find largest index(i) satisfies arr[i-1] < arr[i]
    i = n - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1

    # End of next_permutation
    if i == 0:
        return False

    # find largest index(j) satisfies a[i-1] < a[j]
    j = n - 1
    while arr[i - 1] >= arr[j]:
        j -= 1

    # swap i-1 and j
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # reverse arr[i:]
    start = i
    end = n - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return True


def prev_permutation(arr: list[T]):

    # size of array
    n = len(arr)

    i = n - 1
    while i > 0 and arr[i - 1] <= arr[i]:
        i -= 1
    if i == 0:
        return False

    j = n - 1
    while arr[i - 1] <= arr[j]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    start = i
    end = n - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return True


def permutations_with_replacement(elements: List[Any], size: int):
    """
    Generate all permutations of a specified size from a set of unique elements, allowing repeated selections.

    Parameters:
    elements (iterable): The collection of unique elements to permute.
    size (int): The number of elements to include in each permutation.

    Returns:
    list of tuples: A list of permutations with replacement, each represented as a tuple.

    Example:
    >>> permutations_with_replacement([1, 2, 3], 2)
    [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    """

    yield from product(elements, repeat=size)


def permutations_with_duplicates(elements: List[Any], size: int):
    """
    Generate all permutations of a specified size from a collection of elements, which may include duplicates.

    Parameters:
    elements (iterable): The collection of elements (which may include duplicates) to permute.
    size (int): The number of elements to include in each permutation.

    Returns:
    list of tuples: A list of permutations considering duplicate elements, each represented as a tuple.

    Example:
    >>> permutations_with_duplicates([1, 1, 2], 2)
    [(1, 1), (1, 2), (2, 1)]
    """

    elements.sort()
    cnt = Counter(elements)
    items = list(cnt.keys())
    items_count = list(cnt.values())

    def find_next(cur: List[Any] = [], remaining_size=size):
        # Permutation Found
        if len(cur) == size:
            yield tuple(cur[:])
            return

        # Pruning
        if len(cur) + remaining_size < size:
            return

        for i in range(len(items)):
            if items_count[i] > 0:
                # items[i] 를 고려해서 탐색
                items_count[i] -= 1
                cur.append(items[i])
                yield from find_next(cur, remaining_size - 1)

                # 탐색후 상쇄해서
                items_count[i] += 1
                cur.pop()

    yield from find_next()
