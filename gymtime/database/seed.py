from .models import Gym, Section
from .db import engine
from sqlmodel import Session, select


with Session(engine) as session:
    # Drop all
    for section in session.exec(select(Section)).all():
        session.delete(section)
    for gym in session.exec(select(Gym)).all():
        session.delete(gym)
    session.commit()

    marino = Gym(slug="marino", name="Marino Center", short_name="Marino")
    squash = Gym(slug="squashbusters", name="Squasbusters Center", short_name="Squash")
    session.add(marino)
    session.add(squash)
    session.commit()

    marino_weight_room = Section(
        slug="weight-room", name="Weight Room", short_name="weight", gym_id=marino.id
    )
    marino_track = Section(
        slug="track", name="Track", short_name="track", gym_id=marino.id
    )
    session.add(marino_weight_room)
    session.add(marino_track)

    squash_floor_four = Section(
        slug="floor-four", name="Flour Four", short_name="four", gym_id=squash.id
    )
    session.add(squash_floor_four)
    session.commit()
