from datetime import datetime

class Vehicle:
    def __init__(self, plate_number, vehicle_type, entry_time):
        self.plate_number = plate_number
        self.vehicle_type = vehicle_type
        self.entry_time = entry_time


class ParkingRecord:
    def __init__(self, vehicle, entry_time):
        self.vehicle = vehicle
        self.entry_time = entry_time
        self.exit_time = None
        self.duration = 0
        self.fee = 0


class Payment:
    def __init__(self, method, amount_paid):
        self.payment_method = method
        self.amount_paid = amount_paid
        self.status = False