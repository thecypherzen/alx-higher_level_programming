#!/usr/bin/python3
"""A script that lists all `State` objects, and corresponding `City` objects,
   +contained in the database `hbtn_0e_101_usa`
   - takes 3 arguments: `mysql username`, `mysql password` and
     _`database name`
   - uses only one query to the db
   - uses the `cities` relationship for all `State` objects
   - results are sorted in ascending order by `states.id` and `cities.id`
     - displayed in the format:
       <state id>: <state name>
       <tab><city id>: <city name>

   - is not executed when imported
"""
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import RelationshipProperty, sessionmaker


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    uri = f"mysql+mysqldb://{user}:{passwd}@localhost/{db}"
    engine = create_engine(uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # fetch all states and cities
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
    session.close()
