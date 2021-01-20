import unittest
from src.customer import Customer
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Nicola", 10)
        self.pub = Pub("The pub", 100)
        
    def test_customer_name(self):
        self.assertEqual("Nicola", self.customer.name)

    def test_customer_has_bought_drink(self):
        self.customer.buy_drink(5, self.pub)
        self.assertEqual(5, self.customer.wallet)
        self.assertEqual(105, self.pub.cash)