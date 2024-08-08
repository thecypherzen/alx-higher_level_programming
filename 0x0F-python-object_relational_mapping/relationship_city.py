#!/usr/bin/python3
""" Defines the City Class"""

from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from relationship_state import Base


# define the class State
class City(Base):
    """Class defining a State
    Links to the MySQL table `cities`

    Attributes:
     - id(:int): column of type int
         - auto-generated, unique integer,
         - not null
         - primary key
     - name(:str): column of a type string
         - maximum 128 chars
         - not null
     - state_id(:int): column of state_id
         - foreign key to states.id
         - not null
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities",
                         cascade="all")

    def __init__(self, name):
        """initialises an instance of state"""
        self.name = name

    def __repr__(self):
        """enables pretty print of state object"""
        return f"{self.state.name}: ({self.id}) {self.name}"
