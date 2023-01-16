"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

def my_output(words):
    for word in words:
        print(f"Тип: {type(word)} содержимое:{word} длина:{len(word)}")

if __name__ == "__main__":
    words = [b'class', b'function', b'method']
    my_output(words)