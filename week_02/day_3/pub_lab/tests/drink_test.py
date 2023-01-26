import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Vodka", 5.00, 6)
    
    def test_has_name(self):
        self.assertEqual("Vodka", self.drink.name)
    
    def test_has_price(self):
        self.assertEqual(5.00, self.drink.price)
    
    def test_has_alcholol_level(self):
        self.assertEqual(6, self.drink.alcohol_level)
    
