'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class DivisionByNull(Exception):
    def __init__(self):
        self.txt = "Делить на ноль нельзя."


dividend = int(input("Введите делимое: "))
divisor = int(input("Введите делитель: "))
try:
    if divisor == 0:
        raise DivisionByNull
except DivisionByNull as err:
    print(err.txt)
else:
    print(f"Частное от деление {dividend} на {divisor} равно {dividend / divisor}")
