from datetime import datetime, timedelta

from sqlalchemy import func
from sqlmodel import Session, select

from ..database.db import engine
from ..database.models import Record


def get_records(
    section_id: int, from_date: datetime, to_date: datetime
) -> "list[Record]":
    """Get gym section records in a specified date range"""

    with Session(engine) as session:
        statement = (
            select(Record)
            .where(Record.section_id == section_id)
            .where(Record.time >= from_date)
            .where(Record.time <= to_date + timedelta(days=1))
        )
        results = session.exec(statement)

        return results.all()


def get_average_for_time(
    section_id: int, day_of_week: int, hour: int, days_back: int
) -> float:
    """Get average count in gym section based on records in the last {days_back} days

    day_of_week: Day of week (1 being Sunday)
    hour: Hour of the day to get the average count
    days_back: Number of days back to find records to use in the average count
    """

    if hour < 0 or hour > 23:
        raise Exception("Invalid day")
    if days_back < 7:
        raise Exception("Invalid number of days back")

    # TODO: use days_back param

    with Session(engine) as session:
        # TODO: use sql AVG(), select only Record.count
        statement = (
            select(Record)
            .where(Record.section_id == section_id)
            # Day of week is 1-indexed
            .where(func.DAYOFWEEK(Record.time) == day_of_week)
            .where(func.extract("hour", Record.time) == hour)
        )
        results = session.exec(statement)

        count = 0
        total_count = 0
        for record in results.all():
            total_count += record.count
            count += 1
        average = total_count / count
        return average
