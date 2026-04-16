from src.models import Product, CartItem, Payment
from src.processor import PaymentProcessor


def main():

    # daftar produk
    product1 = Product("Laptop", 7000000)
    product2 = Product("Mouse", 150000)

    # keranjang
    cart = [
        CartItem(product1, 1),
        CartItem(product2, 2)
    ]

    # hitung total
    total_price = PaymentProcessor.calculate_total(cart)

    print("Total harga:", total_price)

    # pembayaran
    amount_paid = float(input("Masukkan jumlah uang: "))
    payment = Payment(amount_paid)

    result = PaymentProcessor.process_payment(total_price, payment)

    print(result["message"])
    print("Kembalian:", result["change"])


if __name__ == "__main__":
    main()