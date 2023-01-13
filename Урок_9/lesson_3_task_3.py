"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1, arg2, arg3):
    """
    Return sum of 2 largest arguments.
    :param arg1:
    :param arg2:
    :param arg3:
    :return:
    """
    sorted_list = sorted([arg1, arg2, arg3])
    return sorted_list[1] + sorted_list[2]

if __name__ == '__main__':
    print(my_func(14, 5, 7))
