'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    # аттрибуты
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # методы
    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        self.direction = direction
        return f'{self.name} повернула {direction}'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'{self.speed} км/ч, что превышает установленный лимит на {self.speed - 60} км/ч'
        return f'{self.speed} км/ч'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'{self.speed} км/ч, что превышает установленный лимит на {self.speed - 40} км/ч'
        return f'{self.speed} км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        Car.__init__(self, speed, color, name, is_police)


ferrari = SportCar(100, 'красная', 'Феррари', False)
lada = TownCar(65, 'белая', 'Лада', False)
solaris = WorkCar(70, 'серая', 'Солярис', False)
ford = PoliceCar(110, 'белая', 'Форд')
print(ferrari.turn('налево'))
print(f'Если {lada.turn("направо")}, тогда {ferrari.stop()}')
print(f'{solaris.go()} со скоростью {solaris.show_speed()}')
print(f'{lada.turn("налево")} со скоростью {lada.show_speed()}')
print(f'{lada.name} - {lada.color}')
print(f'{lada.name} - полицейская машина? {lada.is_police}')
print(f'{ford.name} - полицейская машина? {ford.is_police}')
print(ferrari.show_speed())