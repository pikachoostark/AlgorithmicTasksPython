import math


def merge_sort(arr, l, r):
    if l < r:
        m = math.floor((l + r) / 2)
        return [merge_sort(arr, l, m)] + [merge_sort(arr, m + 1, r)]


lst = [15, 7, 2, 4, 2, 0, 5, 12, -5, 3]
print(merge_sort(lst, 0, 10))
