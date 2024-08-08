#!/usr/bin/python3
"""A script that deletes all `State objects` with a name containing
   +the letter a from `hbtn_0e_6_usa`
   - takes 3 arguments: `mysql username`, `mysql password` and
     _`database name`
   - imports `State` and `Base` from `model_state`
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

    # get state objects and delete them
    states = session.query(State).filter(State.name.ilike("%a%")).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
