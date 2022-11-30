"""
Задание 2
Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3
и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
countries = []
while True:
    country = input("Введите страну: ")
    if country == "":
        break
    countries.append(country)
    capital = input("Введите столицу: ")
    if capital == "":
        break
    countries.append(capital)
print("Введен список:        ", countries)

for index, value in enumerate(countries):
    if index % 2:
        temp = countries[index]
        countries[index] = countries[index - 1]
        countries[index - 1] = temp

print("Переставленный список:", countries)
