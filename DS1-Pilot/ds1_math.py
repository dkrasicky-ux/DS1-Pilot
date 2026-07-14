def risk_level(variance: int) -> str:
    """Return a simple risk label based on variance."""
    if variance <= 0:
        return "Low"
    if variance <= 3:
        return "Medium"
    return "High"
