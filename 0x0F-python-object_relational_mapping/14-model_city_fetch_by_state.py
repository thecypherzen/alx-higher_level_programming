#!/usr/bin/python3
"""A script that prints all `City objects` from the db `hbtn_0e_14_usa`
   - takes 3 arguments: `mysql username`, `mysql password` and
     _`database name`
   - imports `State` and `Base` from `model_state`
   - results are sorted in ascending order by `cities.id`
     - displayed in the format: <state name>: (<city id>) <city name>
   - is not executed when imported
"""
import sys
from model_city import City
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

    # get city objects and print them
    cities = session.query(City).all()
    for city in cities:
        print(city)

    session.close()
