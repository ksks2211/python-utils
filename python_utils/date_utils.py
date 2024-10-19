from datetime import datetime


def current_datetime(include_time=False):
    """Return a string of the current date, and optionally time, with custom separator."""
    format_str = "%Y-%m-%d"
    if include_time:
        format_str += "T%H:%M:%S"  # Using 'T' as a separator between date and time.
    return datetime.now().strftime(format_str)
