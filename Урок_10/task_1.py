'''
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ
'''
from Урок_7.task_3 import Worker, Position
# Берем классы Worker и Position из задания 3 урока 7

class GoodName:
    '''
    Проверяем правильность написания имени или фамилии
    '''
    def __set__(self, instance, value):
        if value == '':
            raise ValueError("Имя или фамилия не должны быть пустой строкой.")
        elif value != value.title():
            raise ValueError("Имя или фамилия должна писаться с заглавной буквы, остальные - строчные.")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class NonNegative:
    '''
    Проверяем неотрицательность ЗП и бонуса
    '''
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class improved_cls_Position(Position):
    # класс на основе старого класса Position, улучшенный дескрипторами
    # создаем дескрипторы
    name = GoodName()
    surname = GoodName()
    wage = NonNegative()
    bonus = NonNegative()

    def __init__(self, name, surname, position, wage, bonus):
        # запускаем проверку дескрипторов
        self.name = name
        self.surname = surname
        self.wage = wage
        self.bonus = bonus
        # а дальше - инициализируем старый класс с уже проверенными атрибутами
        super().__init__(name, surname, position, wage, bonus)


if __name__ == "__main__":
    employee = improved_cls_Position("Иван", "Иванов", "Менеджер", 50000, 30000)
    employee2 = improved_cls_Position("Наталья", "Иванова", "Бухгалтер", 60000, 40000)
    print(employee.get_full_name())
    print(employee.get_total_income())
    print(employee2.get_full_name())
    print(employee2.get_total_income())
