#!/usr/bin/python3i
""" Script that adds the State object
 “Louisiana” to the database hbtn_0e_6_usa """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                        .format(sys.argv[1],
                                sys.argv[2],
                                sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    session = Session()

    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    print(louisiana.id)
