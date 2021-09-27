# https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/python
# На вход программе подаётся последовательность строк.
# Вам необходимо отсортировать её лексикографически (регистрозависимо, по значениям в кодировке ASCII),
#       а затем верните первое значение.
# Возвращённое значение должно быть строкового типа и содержать "***" между каждым знаком.
# Вам НЕ нужно извлекать или добавлять значения в исходный массив.


def two_sort(array):
    # Объявим пустую строку для будущего ответа.
    ans_str = ''
    # Вычислим минимальное значение в исходном массиве.
    min_str = min(array)
    # В цикле добавим три символа "*" после каждой буквы, последовательно внося их в объявленную пустую строку.
    for letter in min_str:
        ans_str += letter
        ans_str += "***"
    # Извлечём лишние, последние три символа.
    ans_str = ans_str[:-3]
    # Вернём полученное значение.
    return ans_str


# Другие гениальные решения:
# def two_sort(array):
#     return '***'.join(min(array)) - красиво и читабельно, окей, 10/10.