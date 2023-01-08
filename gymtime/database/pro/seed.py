from datetime import datetime

from sqlmodel import Session, select

from ..db import engine
from ..models import Gym, Record, Section


def main():
    with Session(engine) as session:
        # Add gyms
        marino = Gym(
            slug="marino",
            name="Marino Center",
            short_name="Marino",
        )
        squash = Gym(
            slug="squashbusters",
            name="Squasbusters Center",
            short_name="Squash",
        )
        session.add(marino)
        session.add(squash)
        session.commit()

        # Add Marino sections
        marino_floor_two = Section(
            gym_id=marino.id,
            slug="marino-floor-two",
            name="Marino Flour Two",
            short_name="Marino F2",
            description="Second Floor",
            c2c_name="Marino Center - 2nd Floor",
        )
        marino_gymnasium = Section(
            gym_id=marino.id,
            slug="marino-gymnasium",
            name="Marino Gymnasium",
            short_name="Marino Gymnasium",
            description="Second Floor",  # confirm this
            c2c_name="Marino Center - Gymnasium",
        )
        marino_weight_room = Section(
            gym_id=marino.id,
            slug="marino-weight-room",
            name="Marino Weight Room",
            short_name="Marino Gymnasium",
            description="Third Floor",
            c2c_name="Marino Center - 3rd Floor Weight Room",
        )
        marino_select_cardio = Section(
            gym_id=marino.id,
            slug="marino-select-cardio",
            name="Marino Select and Cardio",
            short_name="Marino Select, Cardio",
            description="Third Floor",
            c2c_name="Marino Center - 3rd Floor Select & Cardio",
        )
        marino_track = Section(
            gym_id=marino.id,
            slug="marino-track",
            name="Marino Track",
            short_name="Marino Track",
            description="Second Floor",
            c2c_name="Marino Center - Track",
        )
        session.add(marino_floor_two)
        session.add(marino_gymnasium)
        session.add(marino_weight_room)
        session.add(marino_select_cardio)
        session.add(marino_track)

        # Add squash sections
        squash_flour_four = Section(
            gym_id=squash.id,
            slug="squash-floor-four",
            name="Squashbusters Flour Four",
            short_name="Squash F4",
            description="Fourth Floor",
            c2c_name="SquashBusters - 4th Floor",
        )

        session.commit()