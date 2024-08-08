#!/usr/bin/python3
"""A script that uses the State ORM Class to perform a query
   +and list all `State` objects from the `database hbtn_0e_6_usa`

   - takes 3 arguments: `mysql username`, `mysql password` and `database name`
   - imports `State` and `Base` from `model_state`
   - lists all state objects from the database:
     - sorted in ascending order by states.id
     - displayed in the format: `SN: <state.name>` EG. `1: California`
   - is not executed when imported
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    uri = f"mysql+mysqldb://{user}:{passwd}@localhost/{db}"
    engine = create_engine(uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query states
    states = session.query(State).all()
    for state in states:
        print(f"{state.id}: {state.name}")
