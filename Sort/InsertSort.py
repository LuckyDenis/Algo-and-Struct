# -*- coding: utf8 -*-

from random import randint


def insert_sort(arr):
    for i in range(len(arr)):
        value = arr[i]
        j = i
        while j and value < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = value


arr = list(randint(1, 100) for i in range(20))
print(*arr)
insert_sort(arr)
print(*arr)
