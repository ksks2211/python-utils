def insertion_sort(arr: list[float]):
    # 배열의 길이만큼 반복
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # key보다 큰 값들을 오른쪽으로 이동
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # 정렬된 위치에 key를 삽입
        arr[j + 1] = key

    return arr
