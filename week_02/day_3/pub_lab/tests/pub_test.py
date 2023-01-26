import unittest
from src.pub import Pub 
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer = Customer("Stuart", 4.00, 20)
        self.customer2 = Customer("Martina", 5.00, 17)
        self.customer3 = Customer("Alice", 5.00, 20)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_can_increase_till(self):
        self.pub.increase_till(100.00)
        self.assertEqual(200.00, self.pub.till)
    
    