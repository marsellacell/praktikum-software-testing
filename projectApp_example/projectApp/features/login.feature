Feature: Fitur Login Pengguna
  Skenario untuk memverifikasi fungsionalitas login sistem.

  Scenario: Login dengan kredensial yang benar (Berhasil)
    Given pengguna berada di halaman login
    When pengguna memasukkan username "admin" dan password "rahasia123"
    Then pengguna harus diarahkan ke Dashboard

  Scenario: Login dengan password yang salah (Gagal)
    Given pengguna berada di halaman login
    When pengguna memasukkan username "admin" dan password "salah"
    Then muncul pesan kesalahan "Password Salah"