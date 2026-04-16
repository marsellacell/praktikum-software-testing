from datetime import datetime

def calculate_duration(entry_time, exit_time):
    if exit_time < entry_time:
        raise ValueError("Waktu keluar tidak valid")

    duration = (exit_time - entry_time).seconds // 3600
    return max(1, duration)