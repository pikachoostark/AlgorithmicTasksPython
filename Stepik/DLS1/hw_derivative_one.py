# Задача - написать функцию, принимающую в качестве аргумента f, eps и возвращает f'
#   При этом вычисление f' происходит по формуле: f' = [f(x + eps) - f(x)] / eps
import numpy as np
import matplotlib.pyplot as plt


def numerical_derivative_1d(f, eps):
    """ Функция для приближённого вычисления производной функции одной переменной:
        :param f: float -> float - произвольная дифференцируемая функция;
        :param eps: float        - максимальная величина приращения по оси oX;

        :return: другая функция, которая приближённо вычисляет производную в точке
    """
    def derivative_func(x):
        """
            :param x: float - точка, в которой нужно вычислить производную

            :return: приближённое значение производной в этой точке
        """
        return (f(x + eps) - f(x)) / eps

    return derivative_func


## ТЕСТЫ:
# Случайная функция-полином для проверки
def polynome(x):
    return 20*x**5 + x**3 - 5*x**2 + 2*x + 2.0

# Производная функции-полинома
def primed_polynome(x):
    return 100*x**4 + 3*x**2 - 10*x + 2.0

# Приближение производной - функция, которую мы написали от выбранной полиномиальной
# Примем значение eps = 1*10^-5
approximation_derivative = numerical_derivative_1d(polynome, 1e-5)

# Создадим одномерный массив равномерно распределённых 100 точек от -2 до 2
grid = np.linspace(-2, 2, 100)
# Флаг для проверки правильности написанной функции
right_flag = True
# Допустимый предел погрешности
tolerance = 0.05
# Лог ошибки
debug_print = []

# Перебираем значения x из нашего массива
for x in grid:
    # Оценка ошибки - модуль разности точной и приблизительной производных
    estimation_error = abs(primed_polynome(x) - approximation_derivative(x))
    # Если ошибка больше допустимого значения погрешности
    if estimation_error > tolerance:
        # Заполним лог ошибки
        debug_print.append((estimation_error, primed_polynome(x), approximation_derivative(x)))
        # Перевесим флаг ошибки
        right_flag = False

# Если ошибка была хоть раз
if not right_flag:
    # Выведем в консоль лог ошибки
    print("Что-то пошло не так!")
    print(debug_print)
    # И два графика производных - приблизительной и истинной
    plt.plot(grid, primed_polynome(grid), label="Истинная производная")
    plt.plot(grid, approximation_derivative(grid), label="Приближённое значение")
    plt.legend()
    plt.show()

# Выведем флаг
print(str(right_flag))
