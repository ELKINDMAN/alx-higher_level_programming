#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state iport Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ = "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    state = state()
    state.name = "Louisiana"
    session.add(state)
    session.commit()

    result = session.query(State).order_by(State.id.asc())
    print(state.id)
