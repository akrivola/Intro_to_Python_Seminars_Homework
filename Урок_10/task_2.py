'''
Создать метакласс для паттерна Синглтон (см. конец вебинара)
'''


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
        return self.__instance


class A(metaclass=Singleton):
    def __init__(self):
        print('Class A')


class B(metaclass=Singleton):
    def __init__(self):
        print('Class B')


# Создадим несколько экземпляров каждого класса и проверим их на идентичность
a_1 = A()
a_2 = A()
b_1 = B()
b_2 = B()

print('a_1 is a_2 — ', a_1 is a_2)
print('b_1 is b_2 — ', b_1 is b_2)
print('a_1 is b_1 — ', a_1 is b_1)
print('a_2 is b_2 — ', a_2 is b_2)
