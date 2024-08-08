#!/usr/bin/python3
"""A script that adds the `State object` “Louisiana”
   +to the database `hbtn_0e_6_usa`
   - takes 3 arguments: `mysql username`, `mysql password` and
     _`database name`
   - imports `State` and `Base` from `model_state`
   - prints new state.id after creation
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

    # create new state and print new_state.id
    new_state = State("Louisiana")
    session.add(new_state)
    session.commit
    state = session.query(State).filter_by(name="Louisiana").first()
    print(state.id)
    session.close()
