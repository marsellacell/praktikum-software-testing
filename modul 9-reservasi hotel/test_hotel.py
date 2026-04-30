import pytest
from hotel_system import HotelReservationSystem
 
@pytest.fixture	
def system():
    return HotelReservationSystem()
 
# =============================================
# TEST SUITE 1: KETERSEDIAAN KAMAR
# =============================================
class TestAvailability:
    def test_kamar_standard_tersedia(self, system):
        result = system.check_availability("standard")
        assert result["available"] == True
        assert result["price_per_night"] == 500000
 
    def test_kamar_suite_tidak_tersedia(self, system):
        result = system.check_availability("suite")
        assert result["available"] == False
 
    def test_kamar_tidak_valid(self, system):
        result = system.check_availability("presidential")
        assert result["available"] == False
 
# =============================================
# TEST SUITE 2: KALKULASI HARGA
# =============================================
class TestPriceCalculation:
    def test_harga_non_member(self, system):
        # Standard 2 malam tanpa diskon: 500000 x 2 = 1.000.000
        result = system.calculate_price("standard", 2, is_member=False)
        assert result == 1000000
 
    def test_harga_member_diskon_10_persen(self, system):
        # Deluxe 2 malam dengan diskon 10%: 800000 x 2 x 0.9 = 1.440.000
        result = system.calculate_price("deluxe", 2, is_member=True)
        assert result == 1440000
 
    def test_tipe_kamar_tidak_valid(self, system):
        result = system.calculate_price("vip", 3)
        assert result is None
 
# =============================================
# TEST SUITE 3: ALUR RESERVASI FUNGSIONAL
# =============================================
class TestReservation:
    def test_reservasi_berhasil_non_member(self, system):
        result = system.make_reservation(
            "Budi Santoso", "standard", "2026-06-01", "2026-06-03"
        )
        assert result["success"] == True
        assert result["nights"] == 2
        assert result["total_price"] == 1000000
        assert "booking_id" in result
 
    def test_reservasi_berhasil_member(self, system):
        result = system.make_reservation(
            "Siti Rahayu", "deluxe", "2026-07-10", "2026-07-12", is_member=True
        )
        assert result["success"] == True
        assert result["total_price"] == 1440000
 
    def test_reservasi_kamar_tidak_tersedia(self, system):
        result = system.make_reservation(
            "Andi", "suite", "2026-08-01", "2026-08-03"
        )
        assert result["success"] == False
        assert "tidak tersedia" in result["message"]
 
    def test_tanggal_checkout_sebelum_checkin(self, system):
        result = system.make_reservation(
            "Dewi", "standard", "2026-06-05", "2026-06-01"
        )
        assert result["success"] == False
 
# =============================================
# TEST SUITE 4: KEAMANAN AKSES DATA
# =============================================
class TestSecurity:
    def test_akses_booking_sendiri_berhasil(self, system):
        res = system.make_reservation("Tamu A", "standard", "2026-09-01", "2026-09-02")
        booking_id = res["booking_id"]
        result = system.get_booking(booking_id, requester_id=booking_id)
        assert result["success"] == True
 
    def test_akses_booking_orang_lain_ditolak(self, system):
        # Tamu A membuat reservasi
        res_a = system.make_reservation("Tamu A", "standard", "2026-09-01", "2026-09-02")
        # Tamu B mencoba mengakses booking Tamu A (simulasi akses ilegal)
        result = system.get_booking(res_a["booking_id"], requester_id="ILLEGAL_ID")
        assert result["success"] == False
        assert "tidak diizinkan" in result["message"]
 
    def test_booking_id_tidak_ditemukan(self, system):
        result = system.get_booking("NOTEXIST")
        assert result["success"] == False