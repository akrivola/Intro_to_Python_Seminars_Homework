'''
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
'''


class Stationary:
    title = None

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки, инструмент - {self.title}')


class Pencil(Stationary):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки, инструмент - {self.title}')


class Handle(Stationary):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки, инструмент - {self.title}')


my_pen = Pen('Ручка')
my_pen.draw()
my_pencil = Pencil('Карандаш')
my_pencil.draw()
my_handle = Handle('Маркер')
my_handle.draw()