'''
Тестирование задания 1 и 2 урока 10
'''
import unittest

from task_1 import improved_cls_Position


class TestDescriptors(unittest.TestCase):

    def test_bad_name1(self):
        self.assertRaises(Exception, improved_cls_Position, "иван", "Иванов", "Менеджер", 0, 0)

    def test_bad_name2(self):
        self.assertRaises(Exception, improved_cls_Position, "Иван", "иванов", "Менеджер", 0, 0)

    def test_bad_name3(self):
        self.assertRaises(Exception, improved_cls_Position, "ИВАН", "ИВАНОВ", "Менеджер", 0, 0)

    def test_no_name(self):
        self.assertRaises(Exception, improved_cls_Position, "", "", "Менеджер", 0, 0)

    def test_bad_value(self):
        self.assertRaises(Exception, improved_cls_Position, "Иван", "Иванов", "Менеджер", -10, -10)
# Запустить тестирование
if __name__ == '__main__':
    employee = improved_cls_Position("Иван", "Иванов", "Менеджер", 50000, 30000)
    unittest.main()
