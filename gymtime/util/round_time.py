from datetime import datetime, timedelta


def round_hour(dt: datetime) -> datetime:
    """Round times to the nearest hour"""

    # TODO: round UP if beyond minute 45 or 50?
    # if dt.minute >= 50:
    #     dt = dt + timedelta(hours=1)

    return dt.replace(
        minute=0,
        second=0,
        microsecond=0,
    )
