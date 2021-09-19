# https://www.codewars.com/kata/5b853229cfde412a470000d0/python
# Напишите функцию, которая принимает два аргумента:
#     dad_years_old - текущий возраст отца;
#     son_years_old - текущий возраст сына;
# Посчитайте сколько лет назад отцу было вдвое больше лет, чем сыну.
# (Если такого числа нет, то через сколько лет ему будет вдвое больше лет, чем сыну)


def twice_as_old(dad_years_old, son_years_old):
    # Запомним текущий возраст отца
    cur_dad_years = dad_years_old
    # Начнём отсчёт с момента рождения сына
    dad_years_old -= son_years_old
    son_years_old -= son_years_old
    # Инкрементируем оба возраста, пока не получим подходящий результат
    while dad_years_old != 2 * son_years_old:
        dad_years_old += 1
        son_years_old += 1
    # Находим разницу с текущим возрастом.
    # (Можно было красивее и экономнее по памяти, но поленился)
    if dad_years_old > cur_dad_years:
        return dad_years_old - cur_dad_years
    else:
        return cur_dad_years - dad_years_old

# Другие гениальные решения:
# def twice_as_old(dad_years_old, son_years_old):
#     return abs(dad_years_old - 2 * son_years_old) - чёрт, это очень красиво.
#                                                   - но надо разобраться почему так можно на бумажке, это не очевидно.
