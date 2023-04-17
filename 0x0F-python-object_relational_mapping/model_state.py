#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    A SQLAlchemy model class for the states table.
    """
    __tablename__ = "states"

    id = Column(Integer(), primary_key=True,
                unique=True, autoincrement=True, nullable=False)
    """
    The primary key for the state,
    which is a unique auto-incrementing integer.
    """

    name = Column(String(128), nullable=False)
    """
    The name of the state, which is a non-null string
    with a maximum length of 128 characters.
    """