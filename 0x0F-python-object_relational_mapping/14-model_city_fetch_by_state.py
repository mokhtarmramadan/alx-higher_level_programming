#!/usr/bin/python3
""" Print the first cites from the database hbtn_0e_6_usa """

import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    places = session.query(State.name, City.id,
                           City.name).filter(State.id == City.state_id)
    for place in places:
        print("{}: ({}) {}".format(place[0], place[1], place[2]))
