#!/usr/bin/python3
""" Print the first State from the database hbtn_0e_6_usa """

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    firstState = session.query(State).first()
    if firstState is None:
        print("Empty")
    else:
        print("{}: {}".format(firstState.id, firstState.name))
