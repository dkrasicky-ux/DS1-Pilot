def calculate_station_load(station_load: dict) -> dict:
    """Return station load percentages based on total active orders."""
    total = sum(station_load.values()) or 1
    return {station: round((count / total) * 100, 1) for station, count in station_load.items()}
