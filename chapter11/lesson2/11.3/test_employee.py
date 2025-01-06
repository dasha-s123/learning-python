from employee import Employee
import unittest

class EmployeeTestCase(unittest.TestCase):
    """Тесты для класса Employee"""

    def setUp(self):
        """Создание модели работника"""
        self.new_employee = Employee('Maksim', "Andreev", 3000)


    def test_give_default_rise(self):
        """Проверяет повышение по умолчанию"""
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.year_salary, 8000)

    def test_give_custom_rise(self):
        """Проверяет повышение по выбору"""
        self.new_employee.give_raise(4000)
        self.assertEqual(self.new_employee.year_salary, 7000)