from src.models import CartItem, Payment

class PaymentProcessor:

    @staticmethod
    def calculate_total(cart_items: list[CartItem]) -> float:
        total = 0
        for item in cart_items:
            total += item.subtotal()
        return total

    @staticmethod
    def process_payment(total_price: float, payment: Payment) -> dict:
        if payment.amount_paid < total_price:
            return {
                "status": "failed",
                "message": "Insufficient payment",
                "change": 0
            }

        change = payment.amount_paid - total_price

        return {
            "status": "success",
            "message": "Payment successful",
            "change": change
        }