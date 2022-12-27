'''
Написать тесты для ДЗ уроков 1-8
1) не менее 10 тестов
2) желательно с разными ф-циями (assertEqual, assertRaises и т.д.)
3) тесты не должны быть вместе с исходным кодом (нужно разместить в разных модулях)

Задание НУЖНО!!!! сдать архивом
'''
import unittest

from lesson_3_task_4 import my_func1, my_func2
from lesson_3_task_1 import division
from lesson_3_task_3 import my_func
from lesson_3_task_5 import collect_values
from lesson_7_task_1 import TrafficLight
from lesson_9_task_3 import DivisionByNull, Divide
from lesson_1_task_7_additional import weekend
from lesson_7_task_3 import Worker, Position


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
        self.assertEqual(my_func(14, 5, 7), 21)

    def test_my_func_and_2(self):
        self.assertEqual(my_func1(5, 7), my_func2(5, 7))

    def test_class(self):
        result = TrafficLight()
        self.assertIsInstance(result, TrafficLight)

    def test_raise_Exception(self):
        self.assertRaises(DivisionByNull, Divide, 5, 0)

    def test_weekend(self):
        yes = 'да', 'Да', 'yes', 'Yes', 'qui', 'Qui'
        self.assertIn(weekend(6), yes)

    def test_classes(self):
        my_position = Position('John','Doe','support worker', 1000, 130)
        self.assertIsInstance(my_position, Worker)


# Запустить тестирование
if __name__ == '__main__':
    unittest.main()
