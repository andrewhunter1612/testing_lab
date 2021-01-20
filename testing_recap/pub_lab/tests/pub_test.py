import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The prancing pony", 100)
        self.drink = Drink("Beer", 2, 6)
        self.food = Food("Burger", 3, 2)
        self.customer = Customer("name", 10, 21)
        self.underage_customer = Customer("name", 10, 16)
        self.pub.add_stocklist(self.drink)
        self.pub.add_food(self.food)


    def test_pub_has_name(self):
        self.assertEqual("The prancing pony", self.pub.name)

    def test_check_pub_cash(self):
        self.assertEqual(100, self.pub.cash)

    def test_pub_drink(self):
        self.assertEqual("Beer", self.pub.stocklist[0].name)

        
    def test_sell_drink_to_overage_customer(self):
        self.pub.check_drink_is_in_stock(self.drink, self.customer)
        self.assertEqual(6, self.customer.drunkenness)
        self.assertEqual(8, self.customer.wallet)
        self.assertEqual(102, self.pub.cash)
        self.assertEqual([], self.pub.stocklist)

    def test_sell_drink_to_underage_customer(self):
        self.pub.check_drink_is_in_stock(self.drink, self.underage_customer)
        self.pub.sell_food(self.food, self.customer)
        self.assertNotEqual(8, self.customer.wallet)
        self.assertNotEqual(102, self.pub.cash)
        self.assertEqual([self.drink], self.pub.stocklist)

    def test_buy_food(self):
        self.pub.check_drink_is_in_stock(self.drink, self.customer)
        self.pub.sell_food(self.food, self.customer)
        self.assertEqual(5, self.customer.wallet)
        self.assertEqual(105, self.pub.cash)
        self.assertEqual(4, self.customer.drunkenness)

    def test_get_total_stock_value(self):
        self.assertEqual(2, self.pub.check_stock())
