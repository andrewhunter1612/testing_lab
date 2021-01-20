import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Jaegerbomb", 3.5, 2)

    def test_drink_has_name(self):
        self.assertEqual("Jaegerbomb", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(3.5, self.drink.price)  

    def test_drink_has_alcohol_test(self):
        self.assertEqual(2, self.drink.alcohol_level)
