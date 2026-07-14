from ds1_core import *
from ds1_math import risk_level
from ds1_station import calculate_station_load
from ds1_utils import format_time
from ds1_time import current_timestamp

# Simulated data for testing
station_load = {"Cutting": 5, "Assembly": 3, "Sides": 2}

print("=== DS1 Test Run ===")
print(f"Timestamp: {current_timestamp()}")
print(f"Formatted time: {format_time(8)}")
print(f"Risk level (variance 4): {risk_level(4)}")
print("Station load percentages:", calculate_station_load(station_load))
print("Core module check complete.")
