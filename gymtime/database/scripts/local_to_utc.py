"""
2023-01-17: Convert all record times from EST (local time) to UTC.
"""

from datetime import datetime, timezone

from sqlmodel import Session, select

from gymtime.database.db import engine
from gymtime.database.models import Record

"""Example:
naive = datetime(year=2023, month=1, day=15, hour=20, minute=30, second=0)
naive_timestamp = datetime.timestamp(naive)

utc_datetime = datetime.fromtimestamp(naive_timestamp, tz=timezone.utc)

print(naive)
print(utc_datetime)
"""

with Session(engine) as session:
    statement = select(Record)
    results = session.exec(statement)

    for record in results.all():
        print(record.time)
        timestamp = datetime.timestamp(record.time)
        utc_datetime = datetime.fromtimestamp(timestamp,tz=timezone.utc)
        print(utc_datetime)
        
        record.time = utc_datetime
        # session.add(record)
    
    # session.commit()