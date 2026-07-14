def assess_station_risk(station_load):
    """
    station_load: dict like {"Cutting": 35, "Assembly": 10, "Sides": 50}
    returns: dict like {"Cutting": "HIGH", "Assembly": "LOW", "Sides": "HIGH"}
    """

    risk = {}

    for station, minutes in station_load.items():
        if minutes < 10:
            risk[station] = "LOW"
        elif minutes < 20:
            risk[station] = "MEDIUM"
        else:
            risk[station] = "HIGH"

    return risk
