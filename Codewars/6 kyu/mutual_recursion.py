# Взаимная рекурсия позволяет нам получить немного веселья от обычной рекурсии
# (это когда функция вызывает сама себя до прекращающего (терминального) условия)
# и позволяет нескольких функциям вызывать друг друга.
# Давайте используем женские и мужские последователи Хофштадтера, чтобы показать этот приём.
# Вам нужно будет создать две функции F(n) и M(n) так, чтобы следующие выражения соблюдались:
#   F(0) = 1
#   M(0) = 0
#   F(n) = n - M(F(n - 1))
#   M(n) = n - F(M(n - 1))
# Не волнуйтесь за отрицательные числа, n всегда будет не меньше нуля.
# https://ru.wikipedia.org/wiki/Последовательность_Хофштадтера - ссылка на источник


# Функция F(n)
def f(n):
    if n == 0:
        return 1
    else:
        return n - m(f(n - 1))


# Функция M(n)
def m(n):
    if n == 0:
        return 0
    else:
        return n - f(m(n - 1))


# Другие гениальные решения:
# from functools import lru_cache  - срежу остальную часть решения, она идентична моей.
#                                  - но вот декоратор меня заинтересовал.
# @lru_cache
# ...
# def f(n): return n - m(f(n-1)) if n else 1 - ну, и очередной умник, конечно
# def m(n): return n - f(m(n-1)) if n else 0 - не быстрее точно, не читабельнее тоже точно. в чём смысл? compete?