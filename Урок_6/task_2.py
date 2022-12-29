"""
2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
оптимизировать, вновь выполнить замеры и подготовить аналитику, что вы сделали
и чего удалось добиться
"""
from memory_profiler import memory_usage

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
def my_func_lists(x, y):
    res = []
    for i in x:
        res.append(my_func(i, y))
    return res

my_func_lists(list(range(10000)), -3)
