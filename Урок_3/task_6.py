"""
Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def my_func(arg):
    def int_func(word):
        return word.title()

    return " ".join([int_func(i) for i in arg.split(" ")])


print(my_func("humpty dumpty sat on a wall humpty dumpty had a great fall"
              " all the kings horses and all the kings men couldnt put hu"
              "mpty together again"))
