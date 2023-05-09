from argparse import ArgumentParser

# We're using 3.8, but zoneinfo was added in 3.9
from backports.zoneinfo import ZoneInfo

from sqlmodel import Session, select

from gymtime.database.db import engine
from gymtime.database.models import Record, Section
from gymtime.scrape.fetch import fetch_all_records


parser = ArgumentParser(prog="Gym Time", description="Controlling gym time scraping")
parser.add_argument("-f", "--fetch", action="store_true")
args = parser.parse_args()

if args.fetch:
    gym_counts = fetch_all_records()

    with Session(engine) as session:
        for gym_count in gym_counts:
            # Find section
            statement = select(Section).where(Section.c2c_name == gym_count.c2c_name)
            results = session.exec(statement)
            if not results:
                print(f"Section `{gym_count.c2c_name}` not found, skipping")
                continue
                
            section = results.one()

            # Add record if not already there
            local_tz = ZoneInfo("America/New_York")
            utc_tz = ZoneInfo("UTC")
            # The time from C2C is in EST, so convert it to UTC first
            time_est = gym_count.time
            time_est = time_est.replace(tzinfo=local_tz)
            time_utc = time_est.astimezone(utc_tz)

            last_record_statement = (
                select(Record)
                .where(Record.section_id == section.id)
                .where(Record.time == time_utc)
            )
            results = session.exec(last_record_statement)
            last_record = results.first()

            if last_record is not None:
                print(f"Skipping `{section.slug}`; this time has already been added")
                continue

            record = Record(
                section_id=section.id,
                time=time_utc,
                count=gym_count.count,
                percent=gym_count.percent,
            )
            session.add(record)

            session.commit()

            print(f"Records added for `{section.slug}`.")
