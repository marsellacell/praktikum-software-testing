class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class CartItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def subtotal(self):
        return self.product.price * self.quantity


class Payment:
    def __init__(self, amount_paid: float):
        self.amount_paid = amount_paid