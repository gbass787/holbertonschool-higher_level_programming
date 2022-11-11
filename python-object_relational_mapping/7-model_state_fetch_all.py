#!/usr/bin/python3
'''Script that lists all State objects from the database hbtn_0e_6_usa'''
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                            .format(user, passwd, database),
                            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)
    for instance in states:
        print("{}: {}".format(instance.id, instance.name))