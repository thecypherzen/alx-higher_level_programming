#!/usr/bin/python3
"""A script that lists all `City` objects, from  the database
   +`hbtn_0e_101_usa`
   - takes 3 arguments: `mysql username`, `mysql password` and
     _`database name`
   - uses only one query to the db
   - uses the `state` relationship to access the `State` object linked
     + linked to a `City` object
   - results are sorted in ascending order by `cities.id`
     - displayed in the format:
       <city id>: <city name> -> <state name>
   - is not executed when imported
"""
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    uri = f"mysql+mysqldb://{user}:{passwd}@localhost/{db}"
    engine = create_engine(uri, pool_pre_ping=True )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # fetch all data
    cities  = session.query(City).order_by(City.id).all()
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state. name}")
    session.close()
