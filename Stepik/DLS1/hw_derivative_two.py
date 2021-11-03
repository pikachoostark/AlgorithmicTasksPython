# Задача - найти минимум функции с помощью градиентного спуска.
from copy import deepcopy
import numpy as np


def grad_descent_v1(f, df, x0=None, lr=0.1, iters=100, callback=None):
    """ Реализация градиентного спуска для функций одной переменной с одним глобальным минимумом
    :param f: float -> float  - функция
    :param df: float -> float - производная функции
    :param x0: float          - начальная точка
    :param lr: float          - learning rate (значение эпсилон)
    :param iters: int         - количество итераций
    :param callback: callable - функция логирования
    :return: float - координата локального (глобального) минимума
    """

    if x0 is None:
        # Если точка на дана - сгенерируем случайную из нормального распределения
        x0 = np.random.uniform()

    # Присваиваем первое значение x
    x = x0
    # Логирование
    callback(x, f(x))

    # Осуществляем заданное число итераций
    for _ in range(iters):
        # Уменьшаем x на lr * df(x)
        x -= lr * df(x)
        # Логирование
        callback(x, f(x))

    return x


def plot_convergence_1d(f, x_steps, y_steps, ax, grid=None, title=""):
    """ Функция для отрисовки шагов градиентного спуска
    :param f: float -> float        - функция, которая минимизируется градиентным спуском;
    :param x_steps: np.array(float) - шаги алгоритма по оси oX;
    :param y_steps: np.array(float) - шаги алгоритма по оси oY;
    :param ax:                      - холст для отрисовки графика;
    :param grid: np.array(float)    - точки отрисовки функции f;
    :param title: str               - заголовок графика
    :return:
    """
    # Отрисовываем заголовок графика полужирным шрифтом 16 пт
    ax.set_title(title, fontsize=16, fontweight="bold")

    # Если точки для отрисовки не заданы
    if grid is None:
        # То берём 100 равномерно распределённых точек между минимумом и максимумом из x_steps
        grid = np.linspace(np.min(x_steps), np.max(x_steps), 100)

    # Для всех точек для отрисовки (x) найдём значения f(x)
    f_grid = [f(item) for item in grid]
    # Построим график x от y
    ax.plot(grid, f_grid)
    # Посчитаем диапазон y
    y_range = np.max(f_grid) - np.min(f_grid)

    # Зададим аргументы для отрисовки стрелок
    arrow_kwargs = dict(linestyle="--", color="grey", alpha=0.4)
    # Затем для каждой точки x, кроме последней, нарисуем стрелку:
    for i, _ in enumerate(x_steps):
        if i + 1 < len(x_steps):
            # Координаты начала стрелки: xi, yi
            # Длина стрелки по осям:     xi+1 - xi, yi+1 - yi
            ax.arrow(
                x_steps[i], y_steps[i],
                x_steps[i+1] - x_steps[i], y_steps[i+1] - y_steps[i],
                **arrow_kwargs
            )

    # Посчитаем количество точек для отрисовки
    n = len(x_steps)
    # Список цветов
    color_list = [(i / n, 0, 0, 1 - i / n) for i in range(n)]
    # Ставим точки x, y этими цветами
    ax.scatter(x_steps, y_steps, c=color_list)
    # Последнюю точку ставим красным
    ax.scatter(x_steps[-1], y_steps[-1], c="red")
    # Подписываем оси
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")


class LoggingCallback:
    """ Класс для логирования шагов градиентного спуска.
        Сохраняет точку (x, f(x)) на каждом шаге.
    """
    def __init__(self):
        self.x_steps = []
        self.y_steps = []

    def __call__(self, x, y):
        self.x_steps.append(x)
        self.y_steps.append(y)


def test_convergence_1d(grad_descent, test_cases, tolerance=1e-2, axes=None, grid=None):
    """ Функция для проверки корректности решения в одномерном случае.
    :param grad_descent           - ваша реализация градиентного спуска;
    :param test_cases: dict(dict) - тесты в виде словаря со следующими ключами:
        - "f"           - функция (обязательно)
        - "df"          - производная функции (обязательно)
        - "x0"          - начальная точка (м.б. None) (опционально)
        - "low", "high" - диапазон для выбора начальной точки (опционально)
        - "answer"      - ответ (обязательно)
    :param tolerance              - предельно допустимое отклонение
    :param axes                   - матрица холстов для отрисовки, по ячейке на тест
    :param grid: np.array(float)  - точки на оси oX для отрисовки тестов
    :return флаг, корректно ли пройдены тесты и лог ошибки в случае неудачи
    """
    # Повесим флаг для проверки корректности
    right_flag = True
    # Зададим также лог ошибки
    debug_log = []

    # Переберём ключи словаря с тестами
    for i, key in enumerate(test_cases.keys()):
        # Формируем входные данные и ответ для алгоритма
        # В текущем тесте запомним ответ
        answer = test_cases[key]["answer"]
        # Осуществим глубокое копирование текущего теста
        test_input = deepcopy(test_cases[key])
        # Удалим из него ответ
        del test_input["answer"]
        # Запустим сам алгоритм
        # Функция логирования - объект вышезаданного класса
        callback = LoggingCallback()
        # Итоговая точка - наша реализация градиентного спуска (со значениями из нашего теста)
        res_point = grad_descent(*test_input.values(), callback=callback)
        # Отрисовываем результаты
        # Если задан холст
        if axes is not None:
            # Берём текущую ячейку
            # np.unravel_index(i, shape=(x, y)) - возвращает индексы i-той по счёту ячейки в двумерном массиве
            ax = axes[np.unravel_index(i, shape=axes.shape)]
            # Шаги для отрисовки берём из функции логирования
            x_steps = np.array(callback.x_steps)
            y_steps = np.array(callback.y_steps)
            # Вызываем функцию для отрисовки
            plot_convergence_1d(
                test_input["f"], x_steps, y_steps,
                ax, grid, key
            )
            # Рисуем две вертикальные линии: в точке полученного и истинного ответа
            #   пунктиром, определёнными цветами.
            ax.axvline(answer, 0, linestyle="--", c="red",
                       label=f"true answer = {answer}")
            ax.axvline(res_point, 0, linestyle="--", c="xkcd:tangerine",
                       label=f"estimate = {np.round(res_point, 3)}")
            ax.legend(fontsize=16)
        # Проверяем, что найденная точка достаточно близко к истинной
        # Если модуль разности полученного и истинного ответа больше допустимого или ответ отсутствует
        if abs(answer - res_point) > tolerance or np.isnan(res_point):
            # Добавим в лог ошибки информацию об этом
            debug_log.append(
                f"Тест '{key}':\n"
                f"\t- ответ: {answer}\n"
                f"\t- вывод алгоритма: {res_point}"
            )
            # И снимем флаг истинности
            right_flag = False
        # Вернём флаг истинности и лог ошибки
        return right_flag, debug_log
