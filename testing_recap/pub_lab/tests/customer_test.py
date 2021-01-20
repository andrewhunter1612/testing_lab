import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Nicola", 10)
        
    def test_customer_name(self):
        self.assertEqual("Nicola", self.customer.name)
