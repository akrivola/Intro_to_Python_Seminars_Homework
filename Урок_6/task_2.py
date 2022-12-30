"""
2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
оптимизировать, вновь выполнить замеры и подготовить аналитику, что вы сделали
и чего удалось добиться
"""
from memory_profiler import memory_usage

'''
    Скрипт #1
    Берем функцию my_func из урока 3 задание 4. Ф-ия возводит в отрицательную степень.
    Пишем функцию my_func_lists, которая выполняет my_func на списком из аргументов и возвращает список,
    чтобы максимально загрузить память. Ф-ия my_func_lists использует списки и добавление в конец списка.
    Улучшаем функцию my_func_lists, добавляя конструктор (ф-ия improved_my_func_lists)
    Результат замеров памяти:
    my_func_lists - Выполнение заняло 0.48046875 Mib памяти
    improved_my_func_lists - Выполнение заняло 0.0078125 Mib памяти
    
    В итоге, использование конструктора вместо добавления в конец списка занимает меньше памяти.
    
'''

from Урок_3.task_4 import my_func


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib памяти")
        return res

    return wrapper


@memory
def my_func_lists(arg):
    res = []
    for i in arg:
        res.append(my_func(i, -3))
    return res


@memory
def improved_my_func_lists(arg):
    for i in arg:
        yield my_func(i, -3)


# my_func_lists(list(range(1, 10000)))
improved_my_func_lists(list(range(1, 10000)))
