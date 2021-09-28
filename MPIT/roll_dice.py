import random


# Функция будет принимать два аргумента: неизвестное наперёд число игральных костей и количество бросков
def roll_dice(*dices, dice_trials=1000000):
    # Заведём словарь для подсчёта результатов бросков
    prob_dict = {}
    # В цикле бросим кости "dice_trials" раз
    for roll in range(dice_trials):
        # Заведём переменную-счётчик результата текущего броска
        result = 0

        # Бросим каждую кость и добавим результат к счётчику
        for dice in dices:
            result += random.randint(1, dice)

        # Затем внесём результат в наш словарь
        if result not in prob_dict:
            prob_dict[result] = 1
        else:
            prob_dict[result] += 1

    # Выведем результат
    print("OUTCOME\tPROBABILITY")
    for result in sorted(prob_dict):
        # Поделим каждый результат на количество бросков и переведём в проценты домножением на 100
        prob_dict[result] /= (dice_trials // 100)
        # Форматированный вывод результата
        print('{}\t\t{:0.2f}%'.format(result, prob_dict[result]))


roll_dice(6, 6)

# Можно было воспользоваться встроенной библиотекой, а точнее модулем collections, вместо словаря.
# import collections
#
#
# def roll_dice(*dices, dice_trials=1_000_000):
#       prob_dict = collections.Counter()
#       for roll in range(dice_trials):
#           prob_dict[sum((randint(1, sides) for sides in dices))] += 1
#
#       print('\nOUTCOME\tPROBABILITY')
#       for outcome in range(len(dices), sum(dices) + 1):
#           print('{}\t{:0.2f}%'.format(outcome), prob_dict[outcome] * 100 / dice_trials))
