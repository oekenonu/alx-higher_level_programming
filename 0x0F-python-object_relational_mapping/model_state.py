#!/usr/bin/python3
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

# declarative base class
class Base(DeclarativeBase):
    pass

class State(Base):
    """Class with id and name attr"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
