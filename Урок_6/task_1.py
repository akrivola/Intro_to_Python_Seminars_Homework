"""
1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени,
оптимизировать, вновь выполнить замеры и подготовить аналитику, что вы сделали
и чего удалось добиться
"""
from timeit import timeit

'''
Из урока 1 задание 3:
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''


def my_func(n):
    sum_digits = 0
    add = 0
    i = 0
    while i < n:
        add += n * 10 ** i
        sum_digits += add
        i += 1
    return sum_digits


def my_func2(n):
    sum_digits = 0
    i = n
    ten = 1
    while i > 0:
        sum_digits += n * ten * i
        ten *= 10
        i -= 1
    return sum_digits


a = 4
print(timeit('my_func(a)', setup='from __main__ import my_func, a'))
print(timeit('my_func2(a)', setup='from __main__ import my_func2, a'))

'''
Заменив возведение в степень на умножение удалось добиться небольшого прироста в скорости
1.1145545141771436
1.0619966173544526

'''