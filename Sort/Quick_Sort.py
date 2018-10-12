# -*- coding: utf8 -*-

from random import randint


def quick_sort_(arr, start, end):
    if start <= end:
        l, r, x = start, end, arr[(start + end) // 2]
        while l <= r:
            while arr[l] < x:
                l += 1
            while arr[r] > x:
                r -= 1
            if l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        quick_sort_(arr, l, end)
        quick_sort_(arr, start, r)


def quick_sort(arr):
    quick_sort_(arr, 0, len(arr) - 1)


arr = list(randint(1, 100) for i in range(20))
print(*arr)
quick_sort(arr)
print(*arr)
