def calculate_station_load(station_load) -> dict:
    """Return station load values from either a station mapping or a list of orders."""
    if isinstance(station_load, list):
        totals = {}
        for order in station_load:
            station = order.get("station")
            prep_time = order.get("prep_time", 0)
            if station is None:
                continue
            totals[station] = totals.get(station, 0) + prep_time
        return totals

    if not isinstance(station_load, dict):
        raise TypeError("station_load must be a dict or a list of order dicts")

    if not station_load:
        return {}

    total = sum(station_load.values()) or 1
    return {station: round((count / total) * 100, 1) for station, count in station_load.items()}
