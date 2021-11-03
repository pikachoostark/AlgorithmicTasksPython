import math

# 3. Рекурсивное умножение
# Вход: x, y - два n-битовых целых числа x >= 0 и y >= 0
# Выход: x * y


def multiply(x, y):
    if y == 0:
        return 0
    z = multiply(x, math.floor(y / 2))
    if y % 2 == 0:
        return 2 * z
    else:
        return x + 2 * z

# Время работы: O(n^2)
