from collections.abc import Mapping


def calculate_station_load(station_load) -> dict:
    """Return station load values from either a station mapping or a list of orders."""
    if station_load is None:
        return {}

    if isinstance(station_load, Mapping):
        if not station_load:
            return {}

        total = sum(station_load.values()) or 1
        return {station: round((count / total) * 100, 1) for station, count in station_load.items()}

    if isinstance(station_load, (list, tuple)):
        totals = {}
        for order in station_load:
            if not isinstance(order, Mapping):
                continue
            station = order.get("station")
            prep_time = order.get("prep_time", 0)
            if station is None:
                continue
            totals[station] = totals.get(station, 0) + prep_time
        return totals

    if hasattr(station_load, "__iter__") and not isinstance(station_load, (str, bytes)):
        totals = {}
        for item in station_load:
            if not isinstance(item, Mapping):
                continue
            station = item.get("station")
            prep_time = item.get("prep_time", 0)
            if station is None:
                continue
            totals[station] = totals.get(station, 0) + prep_time
        return totals

    return {}
