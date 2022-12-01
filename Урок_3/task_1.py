"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""


def division(arg1, arg2):
    """
    Выполнить деление arg1 на arg2
    :param arg1:
    :param arg2:
    :return: частное
    """
    try:
        return arg1 / arg2
    except ZeroDivisionError:
        return "Ошибка: деление на 0"


print(division(float(input("Введите число #1:")), float(input("Введите число #2:"))))
