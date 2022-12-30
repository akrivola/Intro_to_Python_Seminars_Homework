"""
1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени,
оптимизировать, вновь выполнить замеры и подготовить аналитику, что вы сделали
и чего удалось добиться
"""
from timeit import timeit
from Урок_2.base_task_2 import switch

from numpy import array

def improved_switch(countries):
    for index, value in enumerate(countries):
        if index % 2:
            countries[index], countries[index - 1] = countries[index - 1], countries[index]
    return countries

# switch_mem([i for i in range(100000)])
# improved_switch(array([i for i in range(10000)]))


print(timeit('switch([i for i in range(100000)])', setup='from __main__ import switch', number=1000))

