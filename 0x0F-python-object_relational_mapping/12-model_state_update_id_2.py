#!/usr/bin/python3
"""A script that changes the name of a `State object` from the
   +database `hbtn_0e_6_usa`
   - takes 3 arguments: `mysql username`, `mysql password` and
     _`database name`
   - imports `State` and `Base` from `model_state`
   - changes the name of the `State` where `id = 2` to `New Mexico`
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
    state = session.query(State).filter_by(id=2).first()
    print(state)
    if state:
        state.name = "New Mexico"
        session.commit()
    session.close()
