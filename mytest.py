#!/usr/bin/python3

from sqlalchemy.orm import declarative_base

Base = declarative_base()
print(Base.__dict__)
