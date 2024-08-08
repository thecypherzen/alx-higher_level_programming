#!/usr/bin/python3
"""A script that creates the `State California` with the `City San Francisco`
   +from the database hbtn_0e_100_usa
   - takes 3 arguments: `mysql username`, `mysql password` and
     _`database name`
   - uses the `cities` relationship for all `State` objects
   - results are sorted in ascending order by `cities.id`
     - displayed in the format: <state name>: (<city id>) <city name>
   - is not executed when imported
"""
import sys
from relationship_city import City
from relationship_state import Base, State
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

    # create the city and state
    san_francisco = City("San Francisco")
    california = State("California")
    san_francisco.state = california

    session.add_all([california, san_francisco])
    session.commit()
    session.close()
