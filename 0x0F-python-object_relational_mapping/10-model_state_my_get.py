#!/usr/bin/python3
"""
prints the State object with the name passed as argument from the database
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)

    if len(argv) == 5:
        stateName = argv[4]

        flage = False
        for state in states:
            if state.name == stateName:
                print(state.id)
                flage = True
        if (flage is False):
            print("Not found")
    else:
        print("Not found")
