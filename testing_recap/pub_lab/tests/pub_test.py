import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The prancing pony", 100)
        self.drink = Drink("Beer", 2, 2)

    def test_pub_has_name(self):
        self.assertEqual("The prancing pony", self.pub.name)

    def test_check_pub_cash(self):
        self.assertEqual(100, self.pub.cash)

    def test_pub_drink(self):
        self.assertEqual("Beer", self.pub.stocklist[0])

        
    def test_sell_drink_to_overage_customer(self):
        customer = Customer("name", 10, 21)
        self.pub.check_drink_is_in_stock(self.drink, customer)
        self.assertEqual(2, customer.drunkenness)
        self.assertEqual(8, customer.wallet)
        self.assertEqual(102, self.pub.cash)
        self.assertEqual([], self.pub.stocklist)

    def test_sell_drink_to_underage_customer(self):
        customer = Customer("name", 10, 16)
        self.pub.check_drink_is_in_stock(self.drink, customer)
        self.assertNotEqual(8, customer.wallet)
        self.assertNotEqual(102, self.pub.cash)
        self.assertEqual(["Beer"], self.pub.stocklist)


