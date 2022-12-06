"""
1) Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
пользователем. Об окончании ввода данных свидетельствует пустая строка.
2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
количества строк, количества слов в каждой строке.
3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их
окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести
фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом
английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
текстовый файл.
5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

# Задание 1
out_f = open("out_file_1.txt", "w", encoding='utf-8')
while True:
    data = input("Input data (press <Enter> to finish: ")
    if data == "":
        break
    out_f.write(data + '\n')
out_f.close()

# Задание 2
with open("input_file_2.txt") as f_obj:
    content = f_obj.readlines()
    print(f"Файл {f_obj.name} содержит {len(content)} строк(у):")
    for i, line in enumerate(content, start=1):
        print(f"Строка # {i}: {len(line.split())} слов(а,о)")

# Задание 3
with open("input_file_3.txt") as f_obj:
    content = f_obj.readlines()
my_sum = 0
print("Оклад < 20000:")
for line in content:
    surname, salary = line.split()
    salary = float(salary)
    if salary < 20000:
        print(surname)
    my_sum += salary
print("Средняя зарплата = ", my_sum / len(content))

# Задание 4
numbers_dict = {"One": 'Один',
                "Two": 'Два',
                "Three": 'Три',
                "Four": 'Четыре'}
with open("input_file_4.txt") as in_obj:
    content = in_obj.read()
for key in numbers_dict.keys():
    content = content.replace(key, numbers_dict.get(key))
with open("out_file_4.txt", "w", encoding='utf-8') as out_obj:
    out_obj.write(content)

# Задание 5
from random import randint

with open("out_file_5.txt", "w", encoding='utf-8') as f_obj:
    for i in range(21):
        f_obj.write(str(randint(1, 100)) + ' ')

with open("out_file_5.txt", encoding='utf-8') as f_obj:
    content = f_obj.read().split()
print(sum([int(el) for el in content]))
