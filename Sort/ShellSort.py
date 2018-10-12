# -*- coding: utf8 -*-

from random import randint


def shell_sort(arr):
    shift = len(arr) // 2
    while shift:
        for i in range(len(arr) - shift):
            j = i
            while j >= 0 and arr[j + shift] < arr[j]:
                arr[j + shift], arr[j] = arr[j], arr[j + shift]
                j -= 1
        shift //= 2


arr = list(randint(1, 100) for i in range(20))
print(*arr)
shell_sort(arr)
print(*arr)
