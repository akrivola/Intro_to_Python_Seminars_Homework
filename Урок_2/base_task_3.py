"""
Задание 3
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
number = int(input("Введите месяц (1-12): "))
if 1 <= number <= 12:
    month_list = ['зима', 'зима', 'весна', 'весна',
                  'весна', 'лето', 'лето', 'лето',
                  'осень', 'осень', 'осень', 'зима']
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
    print(f"Время года из list: {month_list[number - 1]}")
    print(f"Время года из dict: {month_dict[number]}")
else:
    print("Ошибка в месяце")
