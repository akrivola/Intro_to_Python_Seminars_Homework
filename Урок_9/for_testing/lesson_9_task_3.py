'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class DivisionByNull(Exception):
    def __init__(self):
        self.txt = "Делить на ноль нельзя."


def Divide(dividend, divisor):
    try:
        if divisor == 0:
            raise DivisionByNull
    except DivisionByNull as err:
        return err.txt
    else:
        return f"Частное от деление {dividend} на {divisor} равно {dividend / divisor}"


if __name__ == '__main__':
    print(Divide(int(input("Введите делимое: ")), int(input("Введите делитель: "))))
