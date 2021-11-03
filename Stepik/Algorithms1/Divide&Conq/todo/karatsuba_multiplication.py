import math


def karatsuba(x, y):
    n = min(len(str(x)), len(str(y)))
    if n == 1:
        return x * y

    xl, xr = int(str(x)[0:math.ceil(n / 2)]), int(str(x)[math.floor(n / 2):])
    yl, yr = int(str(y)[0:math.ceil(n / 2)]), int(str(y)[math.floor(n / 2):])

    p_fst = karatsuba(xl, yl)
    p_snd = karatsuba(xr, yr)
    p_trd = karatsuba(xl + xr, yl + yr)

    return p_fst * 2 ** (2 * math.floor(n / 2) + (p_trd - p_fst - p_snd) * 2 ** (math.floor(n / 2)) + p_snd)


print(karatsuba(1101, 1011))
