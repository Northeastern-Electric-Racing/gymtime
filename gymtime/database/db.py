import os

from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine

from . import models

load_dotenv()

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url)
