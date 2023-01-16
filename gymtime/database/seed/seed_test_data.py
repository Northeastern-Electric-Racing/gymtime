from ..models import Gym, Section, Record
from ..db import engine
from sqlmodel import Session, select
from datetime import datetime


def main():
    with Session(engine) as session:
        # marino = Gym(
        #     slug="marino",
        #     name="Marino Center",
        #     short_name="Marino",
        # )
        # squash = Gym(
        #     slug="squashbusters", name="Squasbusters Center", short_name="Squash"
        # )
        # session.add(marino)
        # session.add(squash)
        # session.commit()

        # marino_weight_room = Section(
        #     slug="weight-room",
        #     name="Weight Room",
        #     short_name="weight",
        #     gym_id=marino.id,
        #     c2c_name="Marino Center - 3rd Floor Weight Room",
        #     description="",  # not needed for testing
        # )
        # marino_track = Section(
        #     slug="track",
        #     name="Track",
        #     short_name="track",
        #     gym_id=marino.id,
        #     c2c_name="Marino Center - Track",
        #     description="",
        # )
        # session.add(marino_weight_room)
        # session.add(marino_track)

        # squash_floor_four = Section(
        #     slug="floor-four",
        #     name="Floor Four",
        #     short_name="four",
        #     gym_id=squash.id,
        #     c2c_name="SquashBusters - 4th Floor",
        #     description="",
        # )
        # session.add(squash_floor_four)
        # session.commit()

        statement_marino_track = select(Section).where(Section.slug == "marino-track")
        results = session.exec(statement_marino_track)
        marino_track = results.one()

        # Sample records
        # Sunday
        marino_track_day1_0500 = Record(
            time=datetime(year=2023, month=1, day=1, hour=5, minute=0),
            count=6,
            percent=6,
            section_id=marino_track.id,
        )
        marino_track_day1_0530 = Record(
            time=datetime(year=2023, month=1, day=1, hour=5, minute=30),
            count=7,
            percent=7,
            section_id=marino_track.id,
        )
        marino_track_day1_0600 = Record(
            time=datetime(year=2023, month=1, day=1, hour=6, minute=0),
            count=6,
            percent=6,
            section_id=marino_track.id,
        )
        marino_track_day1_0630 = Record(
            time=datetime(year=2023, month=1, day=1, hour=6, minute=30),
            count=3,
            percent=3,
            section_id=marino_track.id,
        )
        marino_track_day1_0700 = Record(
            time=datetime(year=2023, month=1, day=1, hour=7, minute=0),
            count=2,
            percent=2,
            section_id=marino_track.id,
        )

        # Monday
        marino_track_day2_0500 = Record(
            time=datetime(year=2023, month=1, day=2, hour=5, minute=0),
            count=3,
            percent=3,
            section_id=marino_track.id,
        )
        marino_track_day2_0530 = Record(
            time=datetime(year=2023, month=1, day=2, hour=5, minute=30),
            count=10,
            percent=10,
            section_id=marino_track.id,
        )
        marino_track_day2_0600 = Record(
            time=datetime(year=2023, month=1, day=2, hour=6, minute=0),
            count=16,
            percent=16,
            section_id=marino_track.id,
        )
        marino_track_day2_0630 = Record(
            time=datetime(year=2023, month=1, day=2, hour=6, minute=30),
            count=13,
            percent=13,
            section_id=marino_track.id,
        )
        marino_track_day2_0700 = Record(
            time=datetime(year=2023, month=1, day=2, hour=7, minute=0),
            count=5,
            percent=5,
            section_id=marino_track.id,
        )

        # Sunday
        marino_track_day8_0500 = Record(
            time=datetime(year=2023, month=1, day=8, hour=5, minute=0),
            count=5,
            percent=5,
            section_id=marino_track.id,
        )
        marino_track_day8_0530 = Record(
            time=datetime(year=2023, month=1, day=8, hour=5, minute=30),
            count=5,
            percent=5,
            section_id=marino_track.id,
        )
        marino_track_day8_0600 = Record(
            time=datetime(year=2023, month=1, day=8, hour=6, minute=0),
            count=6,
            percent=6,
            section_id=marino_track.id,
        )

        # Monday
        marino_track_day9_0500 = Record(
            time=datetime(year=2023, month=1, day=9, hour=5, minute=0),
            count=8,
            percent=8,
            section_id=marino_track.id,
        )
        marino_track_day9_0530 = Record(
            time=datetime(year=2023, month=1, day=9, hour=5, minute=30),
            count=9,
            percent=9,
            section_id=marino_track.id,
        )
        marino_track_day9_0600 = Record(
            time=datetime(year=2023, month=1, day=9, hour=6, minute=0),
            count=8,
            percent=8,
            section_id=marino_track.id,
        )

        session.add(marino_track_day1_0500)
        session.add(marino_track_day1_0530)
        session.add(marino_track_day1_0600)
        session.add(marino_track_day1_0630)
        session.add(marino_track_day1_0700)
        session.add(marino_track_day2_0500)
        session.add(marino_track_day2_0530)
        session.add(marino_track_day2_0600)
        session.add(marino_track_day2_0630)
        session.add(marino_track_day2_0700)
        session.add(marino_track_day8_0500)
        session.add(marino_track_day8_0530)
        session.add(marino_track_day8_0600)
        session.add(marino_track_day9_0500)
        session.add(marino_track_day9_0530)
        session.add(marino_track_day9_0600)
        session.commit()
