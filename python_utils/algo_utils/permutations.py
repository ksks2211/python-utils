from typing import TypeVar

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
