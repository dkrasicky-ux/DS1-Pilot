from ds1_utils import format_time
from ds1_math import risk_level
from ds1_station import calculate_station_load
from ds1_time import current_timestamp

print("=== DS1 Module Test ===")
print("Timestamp:", current_timestamp())
print("Formatted time:", format_time(8))
print("Risk level (variance 4):", risk_level(4))
print("Station load:", calculate_station_load({"Cutting": 5, "Assembly": 3, "Sides": 2}))
