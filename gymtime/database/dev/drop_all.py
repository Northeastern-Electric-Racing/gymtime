from sqlmodel import Session, select

from ..db import engine
from ..models import Gym, Section, Record


def main():
    with Session(engine) as session:
        # Drop all (there's probably a better way to do this)
        for record in session.exec(select(Record)).all():
            session.delete(record)
        for section in session.exec(select(Section)).all():
            session.delete(section)
        for gym in session.exec(select(Gym)).all():
            session.delete(gym)
        session.commit()