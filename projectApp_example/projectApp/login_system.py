# login_system.py

class LoginSystem:
    def __init__(self):
        # Data user sederhana sebagai simulasi database
        self.registered_users = {
            "admin": "rahasia123",
            "asisten": "labinformatika"
        }

    def verify(self, username, password):
        """
        Fungsi untuk memverifikasi kredensial login.
        Mengembalikan 'SUCCESS' jika benar, 
        atau kode error spesifik jika salah.
        """
        if username in self.registered_users:
            if self.registered_users[username] == password:
                return "SUCCESS"
            else:
                return "ERROR_PWD"
        else:
            return "ERROR_USER"

# Kode ini bisa diuji secara manual (opsional)
if __name__ == "__main__":
    app = LoginSystem()
    print(f"Test Success: {app.verify('admin', 'rahasia123')}")
    print(f"Test Fail: {app.verify('admin', 'salah')}")