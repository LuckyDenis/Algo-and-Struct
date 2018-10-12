# -*- coding: utf8 -*-


def bin_found(arr, found):
    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == found:
            return middle
        elif arr[middle] < found:
            start = middle + 1
        else:
            end = middle - 1
    return False


arr = list(i for i in range(1, 40, 2))
print(*arr)
print(bin_found(arr, 3))
print(bin_found(arr, 2))
