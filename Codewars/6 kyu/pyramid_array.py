# https://www.codewars.com/kata/515f51d438015969f7000013/python
# Напишите функцию, которой подаётся число n >= 0, и она возвращает
# массив, состоящий из подмассивов восходящей длины.
#
# pyramid(0) => [ ]
# pyramid(1) => [ [1] ]
# pyramid(2) => [ [1], [1, 1] ]
# pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
#
# Примечание: подмассивы должны заполняться за одну секунду.
def pyramid(n):
    pyramid_array = []
    number_array = []
    for i in range(n):
        number_array.append(1)
        pyramid_array.append(number_array.copy())
    return pyramid_array

# Другие гениальные решения:
#   def pyramid(n):
#       return [ [1] * i for i in range(1, n+1) ] - красиво и лаконично, ничего не скажешь.
