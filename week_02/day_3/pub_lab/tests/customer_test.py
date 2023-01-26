import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Stuart", 10.00, 19)
    
    def test_has_name(self):
        self.assertEqual("Stuart", self.customer.name)
    
    def test_has_wallet(self):
        self.assertEqual(10.00, self.customer.wallet)
    
    def test_has_age(self):
        self.assertEqual(19, self.customer.age)
    
    def test_has_drunkness_zero(self):
        self.assertEqual(0, self.customer.drunkness)
    
    def test_can_decrease_wallet(self):
        self.customer.decrease_wallet(5.00)
        self.assertEqual(5.00, self.customer.wallet)