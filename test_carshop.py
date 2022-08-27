import unittest
from unittest import mock
from carshop import CarRental, Customer, VIP



class TestCarRental(unittest.TestCase):

    PRICE_LESS_THAN_A_WEEK = {"HATCHBACK":30, "SEDAN":50, "SUV":100}
    PRICE_MORE_THAN_A_WEEK = {"HATCHBACK":25, "SEDAN":40, "SUV":90}
    VIP_PRICE = {"HATCHBACK":20, "SEDAN":35, "SUV":80}

    def test_display_stock_and_prices(self):
        rentalshop = CarRental()
        self.assertIsNone(rentalshop.display_stock_and_prices())


class TestCustomer(unittest.TestCase):

    @mock.patch("carshop.input", create = True)
    def test_returncar(self, mocked_input):
        customer = Customer()
        mocked_input.side_effect = [1234]
        self.assertEqual(customer.returncar(), 1234)


    
if __name__ == "__main__":
    unittest.main()
    
  




    

  