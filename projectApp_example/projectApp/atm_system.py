class SimpleATM:
    def __init__(self, balance=500000):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        # LATIHAN: Lengkapi logika penarikan di sini
        # Syarat: Berhasil jika amount <= balance. 
        # Gagal jika amount > balance atau amount <= 0.
        if amount <= 0 or amount > self.balance:
            return False
        
        self.balance -= amount
        return True