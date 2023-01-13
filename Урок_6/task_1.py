"""
1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени,
оптимизировать, вновь выполнить замеры и подготовить аналитику, что вы сделали
и чего удалось добиться
"""
from timeit import timeit
from Урок_2.base_task_2 import switch

import numpy as np

def improved_switch(countries):
    c = countries
    for index, value in enumerate(countries):
        if index % 2:
            countries[index], countries[index - 1] = countries[index - 1], countries[index]
    return countries

#print(switch([i for i in range(100000)]))
#print(improved_switch(array([i for i in range(10000)])))


#print(timeit('switch([i for i in range(100000)])', setup='from __main__ import switch', number=1000))
# 24.00459263997618

print(timeit('improved_switch([i for i in range(100000)])', number=1000, globals=globals()))
# 25.81123218301218
a=np.array([i for i in range(100000)])
print(a)
print(improved_switch(a))