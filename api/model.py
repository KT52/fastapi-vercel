from sqlalchemy import Column, Integer, String
from .database import Base


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    publisher = Column(String)