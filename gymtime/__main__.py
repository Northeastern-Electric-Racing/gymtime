from argparse import ArgumentParser
from sqlmodel import Session, select

from gymtime.scrape.fetch import fetch_all_records
from gymtime.database.db import engine
from gymtime.database.models import Record, Section
from gymtime.util.round_time import round_hour

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
            section = results.one()

            # Add record if not already there
            time = round_hour(gym_count.time)

            last_record_statement = (
                select(Record)
                .where(Record.section_id == section.id)
                .where(Record.time == time)
            )
            results = session.exec(last_record_statement)
            last_record = results.first()

            if last_record is not None:
                print(f"Skipping `{section.slug}`; this time has already been added")
                continue

            record = Record(
                section_id=section.id,
                time=time,
                count=gym_count.count,
                percent=gym_count.percent,
            )
            session.add(record)

            session.commit()

            print("Records added.")
