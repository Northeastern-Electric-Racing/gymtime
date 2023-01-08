from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship, create_engine
from sqlalchemy.orm import RelationshipProperty


class Gym(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    slug: str
    name: str
    short_name: str

    # sections: List["Section"] = Relationship(back_populates="gym")
    sections: List["Section"] = Relationship(
        back_populates="gym",
        sa_relationship=RelationshipProperty(
            "Section",
            primaryjoin="foreign(Gym.id) == Section.gym_id",
            uselist=True,
        ),
    )


class Section(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    slug: str
    name: str
    short_name: str
    c2c_name: str  # Name on Connect2Concepts website
    description: str

    # gym_id: Optional[int] = Field(default=None, foreign_key="gym.id")
    # gym: Optional[Gym] = Relationship(back_populates="sections")
    gym_id: Optional[int] = Field()
    gym: Optional[Gym] = Relationship(
        back_populates="sections",
        sa_relationship=RelationshipProperty(
            "Gym",
            primaryjoin="foreign(Section.gym_id) == Gym.id",
            uselist=False,
        ),
    )

    # records: List["Record"] = Relationship(back_populates="section")
    records: List["Record"] = Relationship(
        back_populates="section",
        sa_relationship=RelationshipProperty(
            "Record",
            primaryjoin="foreign(Section.id) == Record.section_id",
            uselist=True,
        ),
    )


class Record(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    time: datetime
    count: int

    # section_id: Optional[int] = Field(default=None, foreign_key="section.id")
    # section: Optional[Section] = Relationship(back_populates="records")
    section_id: Optional[int] = Field()
    section: Optional[Section] = Relationship(
        back_populates="records",
        sa_relationship=RelationshipProperty(
            "Section",
            primaryjoin="foreign(Record.section_id) == Section.id",
            uselist=False,
        ),
    )
