'''
Написать тесты для ДЗ уроков 1-8
1) не менее 10 тестов
2) желательно с разными ф-циями (assertEqual, assertRaises и т.д.)
3) тесты не должны быть вместе с исходным кодом (нужно разместить в разных модулях)

Задание НУЖНО!!!! сдать архивом
'''
import unittest

import Урок_9.for_testing.lesson_3_task_4
from Урок_9.for_testing.lesson_3_task_1 import division
from Урок_9.for_testing.lesson_3_task_3 import my_func
from Урок_9.for_testing.lesson_3_task_4 import my_func, my_func2


class TestDivision(unittest.TestCase):
    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass

    def test_division(self):
        r = division(100, 5)
        self.assertEqual(r, 20)

    def test_division_by_zero(self):
        r = division(100, 0)
        self.assertEqual(r, "Ошибка: деление на 0")

    def test_my_func(self):
        self.assertEqual(Урок_9.for_testing.lesson_3_task_3.my_func(14, 5, 7), 21)

    def test_my_func_and_2(self):
        self.assertEqual(Урок_9.for_testing.lesson_3_task_4.my_func(5, 7),
                         Урок_9.for_testing.lesson_3_task_4.my_func2(5, 7))


# Запустить тестирование
if __name__ == '__main__':
    unittest.main()
