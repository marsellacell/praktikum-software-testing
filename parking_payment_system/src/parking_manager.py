from datetime import datetime
from src.models import Vehicle, ParkingRecord
from src.pricing_rules import calculate_fee
from src.utils import calculate_duration
from src.payment_processor import process_payment


class ParkingManager:
    def __init__(self):
        self.active_parking = {}

    def vehicle_entry(self, plate, vehicle_type):
        if plate in self.active_parking:
            raise ValueError("Kendaraan sudah masuk")

        vehicle = Vehicle(plate, vehicle_type, datetime.now())
        record = ParkingRecord(vehicle, vehicle.entry_time)

        self.active_parking[plate] = record

    def vehicle_exit(self, plate, payment_method, amount_paid):
        if plate not in self.active_parking:
            raise ValueError("Kendaraan tidak ditemukan")

        record = self.active_parking[plate]
        record.exit_time = datetime.now()

        duration = calculate_duration(record.entry_time, record.exit_time)
        fee = calculate_fee(record.vehicle.vehicle_type, duration)

        if not process_payment(payment_method, amount_paid, fee):
            raise ValueError("Pembayaran kurang")

        record.duration = duration
        record.fee = fee

        del self.active_parking[plate]

        return record