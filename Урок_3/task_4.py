"""
Программа принимает действительное положительное число x
и целое отрицательное число y. Необходимо выполнить возведение
числа x в степень y. Задание необходимо реализовать в виде функции
my_func(x, y). При решении задания необходимо обойтись без встроенной
функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора *.
Второй — более сложная реализация без оператора *, предусматривающая использование цикла.
"""


def my_func(x, y):
    """
    Raise x to the power of y.
    :param x: real positive number.
    :param y: integer negative number.
    :return: real number (x to the power of y).
    """
    res = 1
    for i in range(abs(y)):
        res *= x
    return 1 / res


def my_func2(x, y):
    """
    Raise x to the power of y for integer x only.
    For real x call my_func()
    :param x: integer positive number.
    :param y: integer negative number.
    :return: real number (x to the power of y).
    """
    if x % 10 == 0:
        res = 0
        for i in range(abs(y)):
            for j in range(x):
                res += x
        return 1 / res
    return my_func(x, y)


print(my_func(3.12, -4))
print(my_func2(3, -4))
