#!/usr/bin/python3
""" City class that inhrits from Base """
from model_state import Base
from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base



class City(Base):
    """ City Class """
    __tablename__ = 'cities'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states_id"), nullable=False)
