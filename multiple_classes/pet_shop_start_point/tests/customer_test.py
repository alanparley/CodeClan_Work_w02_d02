import unittest

from classes.customer import Customer
from classes.pet import Pet

class TestCustomer(unittest.TestCase):
    def setUp(self):                                                # these are the values set to the various data at the start of the program and the values to which they will be reset after each test.
        self.customer = Customer("Jack Jarvis", 1000)
        self.pet =  Pet("Blue", "cat", "British Shorthair", 500)

    def test_customer_has_name(self):
        self.assertEqual("Jack Jarvis", self.customer.name)

    def test_customer_has_cash(self):
        self.assertEqual(1000, self.customer.cash)


    def test_pets_start_at_0(self):
        self.assertEqual(0, self.customer.pet_count())              # this means that the pet_count property for he self.customer should be a list and the return from that list length shuld be zero


    def test_can_add_pet(self):
        self.customer.add_pet(self.pet)
        self.assertEqual(1, self.customer.pet_count())


    def test_can_get_total_pet_cost(self):                                                                      # this test has a "get" so we should expect a RETURN statement from the method used.
        
        # We have self.customer and self.customer.pets is an empty list. 
        
        self.customer.add_pet(self.pet)
        self.customer.add_pet(self.pet)
        self.customer.add_pet(self.pet)
        
        # After calling these three lines self.customer.pets will look like [self.pet, self.pet, self.pet]
        
        self.assertEqual(1500, self.customer.get_total_value_of_pets())                                         # we expect a return based on this line because something has to come back from the reference which is the name of the function not the same of a data store.

        # 