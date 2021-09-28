def solve_sudoku(puzzle):
    # Создадим копию нашего судоку
    solved_puzzle = puzzle.copy()
    # Заменим каждый 0 на строку со всеми цифрами 1-9
    for sudoku_string in solved_puzzle:
        for digit in range(len(sudoku_string)):
            if sudoku_string[digit] == 0:
                sudoku_string[digit] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Уберём очевидно невозможные варианты, которые уже есть в заданном судоку

    def clean_up(solved_puzzle=solved_puzzle):
        for string_index in range(len(solved_puzzle)):
            for column_index in range(len(solved_puzzle[string_index])):
                if type(solved_puzzle[string_index][column_index]) == int:
                    digit = solved_puzzle[string_index][column_index]
                    # Переберём строку с этим индексом:
                    for element in solved_puzzle[string_index]:
                        if type(element) == list and digit in element:
                            element.pop(element.index(digit))
                    # Переберём столбцы с этим индексом
                    for iterator in range(len(solved_puzzle)):
                        element = solved_puzzle[iterator][column_index]
                        if type(element) == list and digit in element:
                            element.pop(element.index(digit))
                    # Переберём квадраты 3х3 для этого числа
                    # Дадим каждому квадрату номер: 1 - 2 - 3
                    #                               4 - 5 - 6
                    #                               7 - 8 - 9
                    # Определим квадрат нашего числа:
                    if string_index <= 2:
                        if column_index <= 2:
                            square_number = 1
                        elif column_index <= 5:
                            square_number = 2
                        else:
                            square_number = 3
                    elif string_index <= 5:
                        if column_index <= 2:
                            square_number = 4
                        elif column_index <= 5:
                            square_number = 5
                        else:
                            square_number = 6
                    else:
                        if column_index <= 2:
                            square_number = 7
                        elif column_index <= 5:
                            square_number = 8
                        else:
                            square_number = 9
                    # Для упрощения объявим словарь, содержащий начальные и конечные индексы
                    #   строк и столбцов для каждого квадрата
                    square_dict = {1: [0, 2, 0, 2],
                                   2: [0, 2, 3, 5],
                                   3: [0, 2, 6, 8],
                                   4: [3, 5, 0, 2],
                                   5: [3, 5, 3, 5],
                                   6: [3, 5, 6, 8],
                                   7: [6, 8, 0, 2],
                                   8: [6, 8, 3, 5],
                                   9: [6, 8, 6, 8]}
                    breakdown = square_dict[square_number]
                    for str_square_index in range(breakdown[0], breakdown[1] + 1):
                        for col_square_index in range(breakdown[2], breakdown[3] + 1):
                            element = solved_puzzle[str_square_index][col_square_index]
                            if type(element) == list and digit in element:
                                element.pop(element.index(digit))

    clean_up()
    # Теперь необходимо пройтись по каждому списку в нашем решении, а в них по каждой цифре
    # Если эта цифра встречается только в этом списке на этой строке/столбце/квадрате, то проставим её вместо
    #   этого списка.
    # После этого нужно будет удалить эту цифру из всех списков строки/столбца/квадрата.
    for string_index in range(len(solved_puzzle)):
        for column_index in range(len(solved_puzzle[string_index])):
            if type(solved_puzzle[string_index][column_index]) == list:
                lst = solved_puzzle[string_index][column_index]
                for digit in lst:
                    unique = 0
                    # Перебираем строку этого списка
                    for element in solved_puzzle[string_index]:
                        if type(element) == list and digit in element:
                            unique += 1
                        if unique >= 2:
                            break
                    if unique == 1:
                        solved_puzzle[string_index][column_index] = digit
                        break
                    # Перебираем столбцы этого списка
                    for iterator in range(len(solved_puzzle)):
                        element = solved_puzzle[iterator][column_index]
                        if type(element) == list and digit in element:
                            unique += 1
                        if unique >= 2:
                            break
                    if unique == 1:
                        solved_puzzle[string_index][column_index] = digit
                        break
                    # Перебираем квадраты
                    # Определим квадрат нашего числа:
                    if string_index <= 2:
                        if column_index <= 2:
                            square_number = 1
                        elif column_index <= 5:
                            square_number = 2
                        else:
                            square_number = 3
                    elif string_index <= 5:
                        if column_index <= 2:
                            square_number = 4
                        elif column_index <= 5:
                            square_number = 5
                        else:
                            square_number = 6
                    else:
                        if column_index <= 2:
                            square_number = 7
                        elif column_index <= 5:
                            square_number = 8
                        else:
                            square_number = 9
                    # Для упрощения объявим словарь, содержащий начальные и конечные индексы
                    #   строк и столбцов для каждого квадрата
                    square_dict = {1: [0, 2, 0, 2],
                                   2: [0, 2, 3, 5],
                                   3: [0, 2, 6, 8],
                                   4: [3, 5, 0, 2],
                                   5: [3, 5, 3, 5],
                                   6: [3, 5, 6, 8],
                                   7: [6, 8, 0, 2],
                                   8: [6, 8, 3, 5],
                                   9: [6, 8, 6, 8]}
                    breakdown = square_dict[square_number]
                    for str_square_index in range(breakdown[0], breakdown[1] + 1):
                        for col_square_index in range(breakdown[2], breakdown[3] + 1):
                            element = solved_puzzle[str_square_index][col_square_index]
                            if type(element) == list and digit in element:
                                unique += 1
                            if unique >= 2:
                                break
                    if unique == 1:
                        solved_puzzle[string_index][column_index] = digit
                        break

    # Почистим наш судоку
    clean_up()

    # TODO... Реализовать методы "Открытые пары" и "Скрытые пары"
    # TODO... Также реализовать определение номера квадрата для элемента в виде вложенной функции, чтобы избежать
    #       TODO... дупликации кода.
    return solved_puzzle


sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 3, 6, 0, 0, 0],
          [0, 0, 0, 8, 0, 0, 0, 1, 2],
          [0, 0, 1, 6, 0, 0, 9, 7, 8],
          [0, 0, 0, 0, 7, 0, 0, 0, 0],
          [0, 0, 5, 0, 0, 0, 0, 2, 4],
          [0, 0, 0, 0, 0, 7, 0, 4, 0],
          [0, 6, 9, 0, 5, 0, 1, 0, 0],
          [3, 0, 0, 0, 0, 0, 0, 0, 0]]

solved_sudoku = solve_sudoku(sudoku)
for string in solved_sudoku:
    print(string)
