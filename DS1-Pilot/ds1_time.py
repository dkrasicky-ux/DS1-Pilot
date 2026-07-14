import time

def current_timestamp() -> str:
    """Return a formatted timestamp for dashboard updates."""
    return time.strftime("%Y-%m-%d %H:%M:%S")
