# -*- coding: utf8 -*-

from random import randint


def select_sort(arr):
    for i in reversed(range(len(arr))):
        max_slot = 0
        for j in range(1, i + 1):
            if arr[max_slot] < arr[j]:
                max_slot = j
        arr[max_slot], arr[i] = arr[i], arr[max_slot]


arr = list(randint(0, 100) for i in range(20))
print(*arr)
select_sort(arr)
print(*arr)
