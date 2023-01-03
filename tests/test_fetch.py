import pytest
from sqlmodel import Session, select
from gymtime.functions.fetch import fetch_records
from gymtime.database.db import engine
from gymtime.database.models import Gym, Section


@pytest.fixture
def marino_track() -> Section:
    with Session(engine) as session:
        marino = session.exec(select(Gym).where(Gym.slug == "marino")).one()
        track_section = session.exec(
            select(Section)
            .where(Section.gym_id == marino.id)
            .where(Section.slug == "track")
        ).one()
        return track_section


def test_init(marino_track: Section):
    assert marino_track.gym_id == 1
    assert marino_track.slug == "track"
    assert marino_track.name == "Track"


def test_fetch_records(marino_track: Section):
    ...
