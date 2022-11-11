#!/usr/bin/python3
'''Script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa'''
import sys
from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, passwd, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(text("name='{}'".format(name)))
    state = states.first()
    if state is None:
        print('Not found')
    else:
        print(state.id)