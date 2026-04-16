VALID_METHODS = ["cash", "e-money", "qr"]

def process_payment(method, amount_paid, total_fee):
    if method not in VALID_METHODS:
        raise ValueError("Metode pembayaran tidak valid")

    if amount_paid < total_fee:
        return False

    return True