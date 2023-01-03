from datetime import datetime
from sqlmodel import Session, select
from ..database.db import engine
from ..database.models import Record


def fetch_records(section_id: int, from_date: datetime, to_date: datetime):
    """Get gym section records in the date range"""

    with Session(engine) as session:
        statement = (
            select(Record)
            .where(Record.section_id == section_id)
            .where(Record.time >= from_date)
            .where(Record.time <= to_date)
        )
        results = session.exec(statement)

        print(results)

        return results.all()
