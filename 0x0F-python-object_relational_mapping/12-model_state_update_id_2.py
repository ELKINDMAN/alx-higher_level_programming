#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

def main():
    """update value in database
    """
    aval = sys.argv[1]
    bval = sys.argv[2]
    cval = sys.argv[3]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(aval, bval, cval), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == 2).first()

    state.name = 'New Mexico'

    session.commit()
    session.close()

    if __name__ == "__main__":
        main()
