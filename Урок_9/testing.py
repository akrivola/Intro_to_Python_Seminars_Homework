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
from Урок_9.for_testing.lesson_3_task_5 import collect_values
from Урок_9.for_testing.lesson_7_task_1 import TrafficLight
from Урок_9.for_testing.lesson_9_task_3 import DivisionByNull, Divide
from Урок_9.for_testing.lesson_1_task_7_additional import weekend


class TestDivision(unittest.TestCase):
    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass

    def test_division(self):
        result = division(100, 5)
        self.assertEqual(result, 20)

    def test_division_by_zero(self):
        result = division(100, 0)
        self.assertEqual(result, "Ошибка: деление на 0")

    def test_collect_values_1(self):
        result, err = collect_values("123 456 789".split(" "))
        self.assertEqual(result, 1368)
        self.assertFalse(err)

    def test_collect_values_2(self):
        result, err = collect_values("123 456 stop".split(" "))
        self.assertEqual(result, 579)
        self.assertTrue(err)

    def test_my_func(self):
        self.assertEqual(Урок_9.for_testing.lesson_3_task_3.my_func(14, 5, 7), 21)

    def test_my_func_and_2(self):
        self.assertEqual(Урок_9.for_testing.lesson_3_task_4.my_func(5, 7),
                         Урок_9.for_testing.lesson_3_task_4.my_func2(5, 7))

    def test_class(self):
        result = TrafficLight()
        self.assertIsInstance(result, TrafficLight)

    def test_raise_Exception(self):
        self.assertRaises(DivisionByNull, Divide, 5, 0)

    def test_weekend(self):
        yes = 'да', 'Да', 'yes', 'Yes', 'qui', 'Qui'
        self.assertIn(weekend(6), yes)


# Запустить тестирование
if __name__ == '__main__':
    unittest.main()
