import unittest
from src.payment_processor import process_payment

class TestPaymentProcessor(unittest.TestCase):

    def test_payment_success(self):
        self.assertTrue(process_payment("cash", 10000, 5000))

    def test_payment_insufficient(self):
        self.assertFalse(process_payment("cash", 2000, 5000))

    def test_invalid_method(self):
        with self.assertRaises(ValueError):
            process_payment("bitcoin", 10000, 5000)


if __name__ == "__main__":
    unittest.main()