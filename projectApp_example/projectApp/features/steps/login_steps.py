from behave import given, when, then

# Contoh variabel mock untuk simulasi sistem
class LoginSystem:
    def verify(self, user, pwd):
        if user == "admin" and pwd == "rahasia123":
            return "SUCCESS"
        else:
            return "ERROR_PWD"

@given('pengguna berada di halaman login')
def step_given(context):
    context.app = LoginSystem()

@when('pengguna memasukkan username "{user}" dan password "{pwd}"')
def step_when(context, user, pwd):
    context.result = context.app.verify(user, pwd)

@then('pengguna harus diarahkan ke Dashboard')
def step_then_success(context):
    assert context.result == "SUCCESS"

@then('muncul pesan kesalahan "Password Salah"')
def step_then_fail(context):
    assert context.result == "ERROR_PWD"