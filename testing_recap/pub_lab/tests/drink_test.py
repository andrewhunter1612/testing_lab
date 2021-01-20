import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Jaegerbomb", 3.5)

    def test_drink_has_name(self):
        self.assertEqual("Jaegerbomb", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(3.5, self.drink.price)  
