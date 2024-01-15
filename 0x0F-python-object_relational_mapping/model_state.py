#!/usr/bin/python3
""" State class that inhrits from Base """
from sqlalchemy import String, Integer, Column, MetaData
from sqlalchemy.ext.declarative import declarative_base


mymetadata = MetaData()
Base = declarative_base()


class State(Base):
    """ State Class """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
