# 오름차순 정렬
from typing import TypeVar

T = TypeVar("T", int, float)


def bubble_sort(arr: list[T]):

    size = len(arr)

    # outer loop
    for i in range(size):
        swapped = False

        # The last i elements are in place after inner loop
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped by inner loop, that means arr is sorted.
        if not swapped:
            break

    return arr


def selection_sort(arr: list[T]):
    size = len(arr)

    for i in range(size - 1):
        min_index = i

        # Assumption : sorted = arr[:i] , not-sorted = arr[i:]
        # Find minimum element's index in the remaining unsorted array
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def insertion_sort(arr: list[T]):
    # 배열의 길이만큼 반복
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # 정렬된 위치에 key를 삽입
        arr[j + 1] = key

    return arr
