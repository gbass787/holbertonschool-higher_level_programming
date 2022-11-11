#!/usr/bin/python3
'''Python file that contains the class definition of a State'''
'''And an instance Base = declarative_base()'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    '''Class representing the table of states'''
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)