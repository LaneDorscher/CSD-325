## Author: Lane Dorscher
## Date:  07/22/2026
## Course: CSD-325
## Assignment: 7.2
## Description: Unit Test cases for city_functions.py's city_country function.



import unittest
from city_functions import city_country

class Test_city_functions(unittest.TestCase):

    def test_city_country(self):
        result = city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile")
        
    def test_city_country_population(self):
        result = city_country("Santiago", "Chile", 5000000)
        self.assertEqual(result, "Santiago, Chile - population 5000000")
    
    def test_city_country_language(self):
        result = city_country("Santiago", "Chile", language="Spanish")
        self.assertEqual(result, "Santiago, Chile, Spanish")

    def test_city_country_language_population(self):
        result = city_country("Santiago", "Chile", 5000000, "Spanish")
        self.assertEqual(result, "Santiago, Chile - population 5000000, Spanish")

    def test_fail_city_country_language_population(self):
        result = city_country("Santiago", "Chile", language="Spanish")
        self.assertNotEqual(result, "Santiago, Chile - population 5000000, Spanish")