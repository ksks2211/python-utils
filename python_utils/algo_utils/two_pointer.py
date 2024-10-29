def merge(sorted_arr1: list[int], sorted_arr2: list[int]):
    """merge two sorted arrays

    Args:
        sorted_arr1 (list[T]): array 1
        sorted_arr2 (list[T]): array 2
    """

    n, m = len(sorted_arr1), len(sorted_arr2)
    i = j = 0
    result = [0.0] * (n + m)

    while i < n or j < m:
        if j >= m or (sorted_arr1[i] < sorted_arr2[j]):
            result[i + j] = sorted_arr1[i]
            i += 1
        else:
            result[i + j] = sorted_arr2[j]
            j += 1
    return result


def find_interval_sum(natural_num_arr: list[int], target: int):

    end = 0
    size = len(natural_num_arr)
    interval_sum = 0

    # Forward start
    for start in range(size):

        # Forward end
        # 종료조건
        #  - interval_sum이 target 과 같거나 커지는 순간
        #  - 마지막 요소까지 interval_sum에 더한 다음
        while interval_sum < target and end < size:
            interval_sum += natural_num_arr[end]
            end += 1

        if interval_sum == target:
            # natural_num_arr[start: end] == target
            yield (start, end)

        interval_sum -= natural_num_arr[start]
