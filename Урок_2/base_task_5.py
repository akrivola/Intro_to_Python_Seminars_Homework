"""
Задание 5
Реализовать структуру «Рейтинг», представляющую собой невозрастающий
набор натуральных чисел. У пользователя необходимо запрашивать новый
элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
my_list = [7, 5, 3, 3, 2]
while True:
    user_input = input("Введите рейтинг: ")
    if user_input == "":
        break
    rating = int(user_input)
    for ind, el in enumerate(my_list):
        # print(ind, el)
        if rating > el:
            my_list.insert(ind, rating)
            break
        if ind == len(my_list) - 1:
            my_list.append(rating)
            break
    print(my_list)
