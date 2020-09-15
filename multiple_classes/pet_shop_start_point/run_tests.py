import unittest                                             # ctrl+backtick/tilde = toggle terminal

from tests.pet_test import TestPet
from tests.customer_test import TestCustomer
from tests.pet_shop_test import TestPetShop

if __name__ == '__main__':
    unittest.main()


# tests run in random order but the assertions within each test run in order. This helps when debugging ssertion by asseration.

