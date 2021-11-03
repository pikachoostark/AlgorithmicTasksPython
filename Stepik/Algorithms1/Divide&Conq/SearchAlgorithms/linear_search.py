# 1. Поиск в неупорядоченном массиве:
# Вход: массив arr[...], ключ element
# Выход: индекс index, такой, что arr[index] == element, или -1, если такого index нет
def linear_search(arr, element):
    for index in range(len(arr)):
        if arr[index] == element:
            return index
    return -1

# Время работы: O(n)
