import unittest
from city_functions import place_formatted_name as pfn


class PlaceFormatedTestCase(unittest.TestCase):
    """Тест для функции place_formatted_name"""

    def test_city_country(self):
        """Правильно ли работают места типа 'Santiago, Chilie'?"""
        formatted_place = pfn('santiago', 'chilie')
        self.assertEqual(formatted_place, 'Santiago, Chilie')

if __name__ == '__main__':
    unittest.main()