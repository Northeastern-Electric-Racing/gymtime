from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship, create_engine


class Gym(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    slug: str
    name: str
    short_name: str

    sections: List["Section"] = Relationship(back_populates="gym")

class Section(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    slug: str
    name: str
    short_name: str

    gym_id: Optional[int] = Field(default=None, foreign_key="gym.id")
    gym: Optional[Gym] = Relationship(back_populates="sections")


# class Record(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     time: datetime
#     count: int  

#     section_id: Optional[int] = Field(default=None, foreign_key="section.id")
#     section: Optional[Section] = Relationship(back_populates="sections")
