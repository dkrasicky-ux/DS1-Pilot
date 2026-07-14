import random

# -----------------------------
# Inventory simulation
# -----------------------------
inventory = {
    "Brisket": 42,
    "Pork": 35,
    "Mac": 50
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
# Core order processor
# -----------------------------
def process_order(item):
    # Base prep times
    base_times = {
        "Brisket Sandwich": 12,
        "Pulled Pork": 10,
        "Mac & Cheese": 5
    }

    # Station mapping
    station_map = {
        "Brisket Sandwich": "Cutting",
        "Pulled Pork": "Assembly",
        "Mac & Cheese": "Sides"
    }

    prep_time = base_times.get(item, 8)
    station = station_map.get(item, "Assembly")

    # Random variance simulation
    variance = random.randint(-2, 6)
    adjusted_time = prep_time + variance

    # Failure point detection
    failure = adjusted_time > prep_time + 3

    # Update station load
    station_load[station] += 1

    # Update inventory
    if item == "Brisket Sandwich":
        inventory["Brisket"] -= 1
    elif item == "Pulled Pork":
        inventory["Pork"] -= 1
    elif item == "Mac & Cheese":
        inventory["Mac"] -= 1

    return {
        "item": item,
        "prep_time": prep_time,
        "adjusted_time": adjusted_time,
        "variance": variance,
        "station": station,
        "failure": failure
    }
