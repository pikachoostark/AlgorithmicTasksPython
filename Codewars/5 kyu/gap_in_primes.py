# https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4/python
# Простые числа находятся не на одном и том же расстоянии друг от друга на числовой прямой.
# Между 2 и 3 = 1, между 3 и 5 = 2, между 7 и 11 = 4.
# Между 2 и 50 существуют следующие пары простых чисел с расстоянием 2 между ними:
# 3-5, 5-7, 11-13, 17-19, 29-31, 41-43
# Интервал между простыми числами (prime gap) длины n - промежуток из n-1 последовательно идущих составных чисел
# между двумя последовательными простыми числами.
# http://mathworld.wolfram.com/PrimeGaps.html
#
# Напишем функцию со следующими параметрами:
#       g (int >= 2) - показывает какой интервал мы ищем;
#       m (int >= 2) - начало перебираемого отрезка (включительно);
#       n (1'100'000 >= int >= m) - конец перебираемого отрезка (включительно);
#
# В примере gap(2, 3, 50) вернём [3, 5] | (3, 5) | {3, 5} - первую пару подходящих чисел.
# Следовательно, функция должна вернуть первую(!) подходящую пару в отрезке.
# Первую пару простых чисел с интервалом g между m и n включительно, если такая пара существует.
# Иначе вернуть null | None | Nothing | 'nil | etc. в соответствии с языком.
# https://en.wikipedia.org/wiki/Prime_gap

# Напишем функцию, определяющую простоту числа.
def is_prime(number):
    # Здесь простая оптимизация:
    # Если число не делится на два, то будем перебирать только нечётные числа,
    # что должно уменьшить количество перебираемых делителей в два раза.
    if number % 2 == 0:
        return number == 2
    iterator = 3
    # Здесь в основе первого условия лежит идея:
    # У любого составного числа n есть собственный (т.е. не равный 1) делитель, не превосходящий sqrt(n)
    # Это позволит уменьшить сложность алгоритма линейного перебора с O(n) до O(sqrt(n))
    while iterator * iterator <= number and number % iterator != 0:
        iterator += 2
    # Если квадрат счётчика перешёл наше число и перебор не закончился раньше, то исходное число - простое.
    return iterator * iterator > number


# Сначала я написал наивный алгоритм перебора делителей.
# Очевидно, такой вариант оказался слишком медленным.
# def is_prime(number):
#     flag = True
#     if (number <= 3):
#         return flag
#     for i in range(2, number//2+1):
#         if number%i == 0:
#             flag = False
#             break
#     return flag


# Эта функция будет решать задачу.
def gap(g, m, n):
    # Последнее простое число
    cur_prime = -1
    # Переберём числа заданного диапазона
    for i in range(m, n+1):
        # Если число - простое
        if is_prime(i):
            # И до этого простых чисел не было
            if cur_prime == -1:
                # То запомним это число
                cur_prime = i
            # Если до этого простые числа уже были
            else:
                # Проверим текущий prime gap на соответствие искомому
                cur_gap = i - cur_prime
                # Если подходит, то возвращаем его
                if cur_gap == g:
                    return [cur_prime, i]
                # Иначе меняем последнее простое число
                cur_prime = i
    # Если перебрали все числа и не нашли ответ, то ответ None.
    return None

# Другие гениальные решения:
# from gmpy2 import next_prime  - интересная библиотека, стоит посмотреть документацию.
# def gap(g, m, n):
#     prev = next_prime(m - 1)
#
#     while prev < n:
#         p = next_prime(prev)
#
#         if p - prev == g:
#             return [prev, p]
#
#         prev = p
# Было интересное решение с реализацией алгоритма Рабина-Миллера, но оно занимает под сотню строк с комментариями.
# def gap(g, m, n):
#
#     def _try_composite(a, d, n, s):
#         if pow(a, d, n) == 1:
#             return False
#         for i in range(s):
#             if pow(a, 2**i * d, n) == n-1:
#                 return False
#         return True # n  is definitely composite
#
#     # Miller-Rabin primarility test (rosettacode implementation)
#     def is_prime(n, _precision_for_huge_n=16):
#         if n in _known_primes or n in (0, 1):
#             return True
#         if any((n % p) == 0 for p in _known_primes):
#             return False
#         d, s = n - 1, 0
#         while not d % 2:
#             d, s = d >> 1, s + 1
#         # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
#         if n < 1373653:
#             return not any(_try_composite(a, d, n, s) for a in (2, 3))
#         if n < 25326001:
#             return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
#         if n < 118670087467:
#             if n == 3215031751:
#                 return False
#             return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
#         if n < 2152302898747:
#             return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
#         if n < 3474749660383:
#             return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
#         if n < 341550071728321:
#             return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
#         # otherwise
#         return not any(_try_composite(a, d, n, s)
#                        for a in _known_primes[:_precision_for_huge_n])
#
#     _known_primes = [2, 3]
#     _known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]
#
#     # Check initial pre-conditions
#     assert((g, m) >= (2, 2))
#     assert(n >= m)
#
#     a, b = None, None
#
#     for current in xrange(m + 1 if m % 2 == 0 else m, n, 2):
#         if is_prime(current):
#             a, b = b, current
#             if a is not None and b is not None and (b - a) == g:
#                     return [a, b]
#
#     return None
# Другой вариант:
# import math
#
# def gap(g, start,stop):
#     k = math.ceil((start - 1)/6)
#     UltPrime ,p1,p2 = 0,0,0
#
#     while p1<=stop or p2<=stop:
#         p1, p2 = 6*k - 1, 6*k + 1
#         if start<=p1<=stop and IsPrime(p1):
#             if (p1 - UltPrime) == g and UltPrime > 0: return [UltPrime,p1]
#             else: UltPrime = p1
#
#         if start<=p2<=stop  and IsPrime(p2):
#             if (p2 - UltPrime) == g and UltPrime > 0: return [UltPrime,p2]
#             else: UltPrime = p2
#
#         k = k + 1
#     return None
#
# def IsPrime(n):
#     d, s = n - 1, 0
#     while not d % 2: d, s = d >> 1, s + 1
#     # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
#     if n < 1373653:         return not any(TryComposite(a, d, n, s) for a in (2, 3))
#     if n < 25326001:        return not any(TryComposite(a, d, n, s) for a in (2, 3, 5))
#     if n < 118670087467:    return [not any(TryComposite(a, d, n, s) for a in (2, 3, 5, 7)),False][n == 3215031751]
#     if n < 2152302898747:   return not any(TryComposite(a, d, n, s) for a in (2, 3, 5, 7, 11))
#     if n < 3474749660383:   return not any(TryComposite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
#     if n < 341550071728321: return not any(TryComposite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
#
# #Test de primalidad de Miller-Rabin
# def TryComposite(a, d, n, s):
#     if pow(a, d, n) == 1: return False
#     for i in range(s):
#         if pow(a, 2**i * d, n) == n-1: return False
#     return True # n is definitely composite
# Также было решение через numpy.
# import numpy as np
#
# sieve = np.ones(12_000_000, dtype=bool)
# sieve[0] = sieve[1] = 0
# sieve[2*2::2] = 0
# for i in range(3, int(len(sieve)**0.5)+1, 2):
#     if sieve[i]:
#         sieve[i*i::i] = 0
# primes = np.array([i for i, x in enumerate(sieve) if x], dtype=int)
#
# def gap(g, m, n):
#     i = primes.searchsorted(m)
#     j = primes.searchsorted(n)
#     for k in range(i, j+1):
#         if primes[k+1] - primes[k] == g:
#             return list(primes[k:k+2])
