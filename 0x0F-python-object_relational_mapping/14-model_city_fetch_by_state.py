#!/usr/bin/python3

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import Base, State

if __name__ == "__main__":
    # Connect to the database using the provided credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    # Create a session object using the engine
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    for cities, state in session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, cities.id, cities.name))
