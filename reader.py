from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Text, ForeignKey, select
from flask_login import UserMixin
from base_class_sql import Base


class Reader(Base, UserMixin):
    __tablename__= "readers"
    def __init__(self,id, password, name):
        self.id=id
        self.name = name
        self.password=password



    id = Column(Integer, primary_key=True)
    name = Column(Text)
    password = Column(Text)
    print('init reader')


    def __repr__(self):
        return f'id:{self.id},{self.name}'