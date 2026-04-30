import uuid
from datetime import datetime
 
ROOM_DATA = {
    "standard": {"price": 500000, "available": True},
    "deluxe":   {"price": 800000, "available": True},
    "suite":    {"price": 1500000, "available": False},
}
 
class HotelReservationSystem:
    def __init__(self):
        self.bookings = {}
 
    def check_availability(self, room_type):
        if room_type not in ROOM_DATA:
            return {"available": False, "message": "Tipe kamar tidak ditemukan"}
        room = ROOM_DATA[room_type]
        return {
            "available": room["available"],
            "room_type": room_type,
            "price_per_night": room["price"]
        }
 
    def calculate_price(self, room_type, nights, is_member=False):
        if room_type not in ROOM_DATA:
            return None
        base_price = ROOM_DATA[room_type]["price"] * nights
        discount = 0.10 if is_member else 0
        total = base_price * (1 - discount)
        return round(total)
 
    def make_reservation(self, guest_name, room_type, check_in, check_out, is_member=False):
        avail = self.check_availability(room_type)
        if not avail["available"]:
            return {"success": False, "message": "Kamar tidak tersedia"}
        try:
            ci = datetime.strptime(check_in, "%Y-%m-%d")
            co = datetime.strptime(check_out, "%Y-%m-%d")
            nights = (co - ci).days
        except ValueError:
            return {"success": False, "message": "Format tanggal tidak valid"}
        if nights <= 0:
            return {"success": False, "message": "Tanggal checkout harus setelah check-in"}
        total = self.calculate_price(room_type, nights, is_member)
        booking_id = str(uuid.uuid4())[:8].upper()
        self.bookings[booking_id] = {
            "guest_name": guest_name,
            "room_type": room_type,
            "check_in": check_in,
            "check_out": check_out,
            "nights": nights,
            "total_price": total,
            "is_member": is_member
        }
        return {"success": True, "booking_id": booking_id, "total_price": total, "nights": nights}
 
    def get_booking(self, booking_id, requester_id=None):
        if booking_id not in self.bookings:
            return {"success": False, "message": "Booking tidak ditemukan"}
        if requester_id and requester_id != booking_id:
            return {"success": False, "message": "Akses tidak diizinkan"}
        return {"success": True, "data": self.bookings[booking_id]}