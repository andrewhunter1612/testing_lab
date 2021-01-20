import unittest
from src.customer import Customer
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Nicola", 10, 21)
        self.pub = Pub("The pub", 100)
        
    def test_customer_name(self):
        self.assertEqual("Nicola", self.customer.name)

    
