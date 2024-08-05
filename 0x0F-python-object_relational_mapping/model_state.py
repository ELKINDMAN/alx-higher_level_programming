#!/usr/bin/python3
""" Class containing the definition of a State
and an instance base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """_summary_

    Args: 
        Base (_type_): _description_
     """
     __tablename__ = "states"
     id = Column('id', Integer, autoincrement=True. primsryKey=True)
     name = Column('name', String(128))
