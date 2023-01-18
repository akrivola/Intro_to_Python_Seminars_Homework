"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
def my_output(word):
    print(f"Тип: {type(word)} содержимое: {word}")

words = ['разработка', 'администрирование', 'protocol', 'standard']

for word in words:
    word_bytes = word.encode('utf-8')
    word_str = word_bytes.decode('utf-8')
    my_output(word)
    my_output(word_bytes)
    my_output(word_str)
