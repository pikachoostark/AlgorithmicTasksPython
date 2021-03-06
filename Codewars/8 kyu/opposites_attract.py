# https://www.codewars.com/kata/555086d53eac039a2a000083/python
# Тимми и Сара считают, что они влюблены друг в друга, но там, где они живут
# они узнают об этом только после того, как сорвут по цветку.
# Если у одного из цветков будет чётное количество лепестков, а у другого - нечётное, это будет значить
# что они влюблены друг в друга.
#
# Напишите функцию, которая будет принимать количество лепестков каждого цветка и возвращать true,
# если они влюблены друг в друга и false, если нет.


def love_func(flower1, flower2):
    return (not flower1 % 2 and flower2 % 2) or (flower1 % 2 and not flower2 % 2)

# Другие гениальные варианты:
#     return (flower1+flower2)%2        - только чётное + нечётное дает нечётное, остальные - чётные.
#     return flower1 % 2 != flower2 % 2 - тоже круто, комментарии излишни.
#     return flower1 % 2 ^ flower2 % 2  - побитовый xor, я и забыл про него.
