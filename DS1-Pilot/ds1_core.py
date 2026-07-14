import random

# -----------------------------
# Inventory simulation
# -----------------------------
inventory = {
    "Brisket": 42,
    "Pork": 35,
    "Chicken": 50
}

# -----------------------------
# Station load simulation
# -----------------------------
station_load = {
    "Cutting": 0,
    "Assembly": 0,
    "Sides": 0
}

# -----------------------------
# Calculate station load from orders
# -----------------------------
def calculate_station_load_from_orders(orders):
    """Calculate total station load based on menu prep times."""
    load = {"Cutting": 0, "Assembly": 0, "Sides": 0}
    
    for order in orders:
        load[order["station"]] += order["prep_time"]
    
    return load
