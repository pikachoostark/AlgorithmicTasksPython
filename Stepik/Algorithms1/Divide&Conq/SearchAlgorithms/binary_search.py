import math

# 2. Поиск в упорядоченном (по неубыванию) массиве
# Вход: упорядоченный массив arr[...], ключ element
# Выход: индекс index, такой, что arr[index] == element, или -1, если такого index нет


def binary_search(arr, element):
    bot = 0
    top = len(arr)-1
    while bot <= top:
        mid = math.floor((bot + top) / 2)
        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            top = mid - 1
        else:
            bot = mid + 1
    return -1

# Время работы: O(log n)
