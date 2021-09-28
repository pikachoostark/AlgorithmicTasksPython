import random
import time


# Аргумент функции - через сколько секунд нужно нажать для победы
def waiting_game(target=random.randint(5, 10)):
    # Задаём условие игроку
    print("Your target time is: " + str(target))

    # Ждём нажатия клавиши ENTER, чтобы начать игру
    input("\n== Press ENTER to start the game! ==")
    # Запомним время начала игры
    start = time.perf_counter()

    # Ждём нажатия клавиши ENTER, чтобы завершить игру
    input("== Press ENTER again after {} seconds...".format(target))
    # Вычислим прошедшее время
    elapsed = time.perf_counter() - start

    # Выведем пользователю сколько времени прошло
    print('\nElapsed time: {0:.3f} seconds'.format(elapsed))

    # Если прошло ровно сколько нужно времени
    if elapsed == target:
        # То поздравим пользователя с попаданием
        print("Right in time!")
    # Если прошло меньше
    elif elapsed < target:
        # Напишем, что нажали кнопку рано
        print("Too fast! {0:.3f} seconds".format(target - elapsed))
    # Если прошло больше
    else:
        # Напишем, что нажали кнопку поздно
        print("Too slow! {0:.3f} seconds".format(elapsed - target))


# Запустим игру
waiting_game()
