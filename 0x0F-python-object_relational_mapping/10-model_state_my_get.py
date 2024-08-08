#!/usr/bin/python3
"""A script that prints the `State object` with the name passed as
   +argument from the database `hbtn_0e_6_usa`
   - takes 4 arguments: `mysql username`, `mysql password`,
     _`database name` and `state name to search`
   - imports `State` and `Base` from `model_state`
   - results must display the `states.id`
      - if no state has the name you searched for, display Not found
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

    # query a state
    state = session.query(State)\
        .filter_by(name=f"{sys.argv[4]}").first()
    if not state:
        print("Not found")
    else:
        print(f"{state.id}")
