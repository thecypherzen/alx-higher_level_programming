#!/usr/bin/python3
""" Defines the State Class and Base"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# define the class State
class State(Base):
    """Class defining a State
    Attributes:
     - id(:int): column of type int
         - auto-generated, unique integer,
         - not null
         - primary key
     - name(:str): column of a type string
         - maximum 128 chars
         - not null
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
