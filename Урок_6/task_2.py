"""
2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
оптимизировать, вновь выполнить замеры и подготовить аналитику, что вы сделали
и чего удалось добиться
"""
from memory_profiler import profile
from copy import deepcopy

@profile
def function_1():
    """Выделяет доп память, не освобождается"""
    x = list(range(10000))
    y = deepcopy(x)
    return y

@profile
def month_from_list(number):
    if 1 <= number <= 12:
        month_list = ['зима', 'зима', 'весна', 'весна',
                      'весна', 'лето', 'лето', 'лето',
                      'осень', 'осень', 'осень', 'зима']
        return month_list[number - 1]
    else:
        print("Ошибка в месяце")

@profile
def month_from_dict(number):
    if 1 <= number <= 12:
        month_dict = {1: 'зима',
                      2: 'зима',
                      3: 'весна',
                      4: 'весна',
                      5: 'весна',
                      6: 'лето',
                      7: 'лето',
                      8: 'лето',
                      9: 'осень',
                      10: 'осень',
                      11: 'осень',
                      12: 'зима'}
        return month_dict[number]
    else:
        print("Ошибка в месяце")
'''
number = int(input("Введите месяц (1-12): "))
print(f"Время года из list: {month_from_list(number)}")
print(f"Время года из dict: {month_from_dict(number)}")
'''
@profile
def my_func3(arg1, arg2, arg3):
    sorted_list = sorted([arg1, arg2, arg3])
    y = deepcopy(sorted_list)
    return sorted_list[1] + sorted_list[2]

@profile
def my_func4(arg1, arg2, arg3):
    return arg1 + arg2 + arg3 - min(arg1, arg2, arg3)


my_func3(14, 5, 7)
my_func4(14, 5, 7)
