from sqlmodel import SQLModel, create_engine
from . import models
from .db import engine

def main():
    SQLModel.metadata.create_all(engine)
