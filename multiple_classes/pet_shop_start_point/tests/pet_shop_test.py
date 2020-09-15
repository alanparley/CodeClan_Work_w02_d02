import unittest

from classes.pet_shop import PetShop
from classes.pet import Pet
from classes.customer import Customer

class TestPetShop(unittest.TestCase):
    def setUp(self):
        self.pet_1 =  Pet("Sir Percy", "cat", "British Shorthair", 500)
        self.pet_2 =  Pet("King Arthur", "dog", "Husky", 900)

        pets = [self.pet_1, self.pet_2]
        self.pet_shop = PetShop("Camelot of Pets", pets, 1000)
#1
    def test_pet_shop_has_name(self):
        self.assertEqual("Camelot of Pets", self.pet_shop.name)

#2
    def test_pet_shop_cash(self):
        self.assertEqual(1000, self.pet_shop.total_cash)
#3

    def test_pet_shop_pets_sold_starts_at_0(self):
        self.assertEqual(0, self.pet_shop.pets_sold)
#4
#stock_count is a method with no arguments passed - it is checking that the number of entries in the list of pets is 2.
# additionally the name of the function indicates that it is counting something!
    def test_pet_shop_stock_count(self):
        self.assertEqual(2, self.pet_shop.stock_count())
#5
# the method increase_pets_sold() doesnt take an arguement so will cause default increase by 1
    def test_increase_pets_sold(self):
        self.pet_shop.increase_pets_sold()              
        self.assertEqual(1, self.pet_shop.pets_sold)
#6

    def test_can_increase_total_cash(self):
        self.pet_shop.increase_total_cash(500)
        self.assertEqual(1500, self.pet_shop.total_cash)
#7
# you dont always add everything to the defsetup because sometimes the data that is being used is only used for one or few tests. Thats why we dont need to have this additional pet in the defsetup list of pets
# this is particularly important when it comes to large or complex testing suites because the larger the startup data structure the longer that the testing will take to run (Zsolt mentioned that cutting down on the defsetup data saved 14 minutes on a 16 minute test at criton.)
    def test_can_add_pet_to_stock(self):
        new_pet = Pet("Lancelot", "dog", "Basset Hound", 750)
        self.pet_shop.add_pet(new_pet)
        self.assertEqual(3, self.pet_shop.stock_count())
#8

    def test_can_remove_pet_from_stock(self):
        self.pet_shop.remove_pet(self.pet_1)
        self.assertEqual(1, self.pet_shop.stock_count())
#9
# this is back to nested objects so tricker than the revious ones
    def test_can_find_pet_by_name(self):
        pet = self.pet_shop.find_pet_by_name("Sir Percy")
        self.assertEqual("Sir Percy", pet.name)    # need to return the entire pet object so that the .name can be run on it in the check
# work until here and #10 will be done with class
#10 - this is an integration test, the other ones were unit tests. unit tests stests for the smallest pieces only.

    def test_can_sell_pet_to_customer(self):
        customer = Customer("Jack Jarvis", 1000)                        # this is the only test which needs a customer which is why the customer is being set within this test and not in the original setup
        self.pet_shop.sell_pet_to_customer("Sir Percy", customer)       # this is the method to write # these are the four things that should then happen
        self.assertEqual(1, customer.pet_count())                       
        self.assertEqual(1, self.pet_shop.stock_count())
        self.assertEqual(1, self.pet_shop.pets_sold)
        self.assertEqual(1500, self.pet_shop.total_cash)
        # no check on the customers cash going down