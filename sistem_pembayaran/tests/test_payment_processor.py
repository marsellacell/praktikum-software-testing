import unittest

from src.models import Product, CartItem, Payment
from src.processor import PaymentProcessor


class TestPaymentProcessor(unittest.TestCase):

    def setUp(self):
        """
        Setup data yang akan digunakan oleh setiap test
        """
        self.product1 = Product("Laptop", 7000000)
        self.product2 = Product("Mouse", 150000)

        self.cart = [
            CartItem(self.product1, 1),
            CartItem(self.product2, 2)
        ]

    def test_calculate_total(self):
        """
        Test apakah total harga dihitung dengan benar
        """
        total = PaymentProcessor.calculate_total(self.cart)
        expected_total = 7000000 + (150000 * 2)

        self.assertEqual(total, expected_total)

    def test_payment_success(self):
        """
        Test pembayaran berhasil jika uang cukup
        """
        total = PaymentProcessor.calculate_total(self.cart)

        payment = Payment(8000000)

        result = PaymentProcessor.process_payment(total, payment)

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["change"], 700000)

    def test_payment_failed(self):
        """
        Test pembayaran gagal jika uang kurang
        """
        total = PaymentProcessor.calculate_total(self.cart)

        payment = Payment(5000000)

        result = PaymentProcessor.process_payment(total, payment)

        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["change"], 0)


if __name__ == "__main__":
    unittest.main()