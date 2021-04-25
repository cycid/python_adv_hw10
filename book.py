from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Text, ForeignKey, select, Sequence
from sqlalchemy.orm import mapper, relationship, Session
from reader import Reader
from base_class_sql import Base

class Book(Base):
    __tablename__= "books"
    def __init__(self,id, title, author, year:int, status=None):
        self.id=id
        self.title=title
        self.author=author
        self.year=year
        self.status=status


    id = Column(Integer, primary_key=True)
    title = Column(Text)
    author = Column(Text)
    year = Column(Integer)
    status = Column(Integer, ForeignKey('readers.id'))







    def __repr__(self):
        return f'{self.title} by {self.author} published in {self.year} in {self.status}'








