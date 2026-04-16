def calculate_fee(vehicle_type, duration):
    rates = {
        "motor": 2000,
        "mobil": 5000,
        "bus": 10000
    }

    if vehicle_type not in rates:
        raise ValueError("Jenis kendaraan tidak valid")

    if duration <= 0:
        return rates[vehicle_type]

    return rates[vehicle_type] * duration