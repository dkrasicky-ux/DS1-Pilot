def format_time(minutes: int) -> str:
    """Return a clean time string for display."""
    if minutes < 1:
        return "Under 1 min"
    return f"{minutes} min"
