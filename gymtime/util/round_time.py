from datetime import datetime, timedelta


def round_hour(dt: datetime) -> datetime:
    """Round times to the nearest hour/half hour"""
    if dt.minute >= 30:
        return dt.replace(
            minute=30,
            second=0,
            microsecond=0,
        )
    else:
        return dt.replace(
            minute=0,
            second=0,
            microsecond=0,
        )
