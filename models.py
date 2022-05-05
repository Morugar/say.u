from sqlalchemy import create_engine, Column, Integer, VARCHAR, String, ForeignKey, PrimaryKeyConstraint
from peewee import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.exc.declarative import declaratuive_base

from config import DATABASE_URL

Base = declarative_base()

def connect_db():
    engine = create_engine(DATABASE_URL, connect_args={})
    session = Session(bind=engine.connect())
    return session

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    login = Column(String)
    password = Column(String)
    token = Column(String)
    email = Column(String)
    social = Column(String)
    location = Column(String)
    age = Column(Integer)
    hobby = Column(String)
    career = Column(String)
    education = Column(String)
    cigaretes = Column(String)
    alcohol = Column(String)
    music = Column(String)
    films = Column(String)
    videogames = Column(String)
    serials = Column(String)
    books = Column(String)
    avatar = Column(String)

class Chats(Base):
    __tablename__ = "chats"
    
    id1 = Column(Integer, ForeignKey("user.id"))
    id2 = Column(Integer, ForeignKey("user.id"))
    location = Column(String)

class Shared(Base):
    __tablename__ = "shared"

    owner_id = Column(Integer, ForeignKey("user.id"))
    shared_id = Column(Integer, ForeignKey("user.id"))
    field = Column(String)