import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, VARCHAR, String, ForeignKey, PrimaryKeyConstraint
from peewee import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from config import DATABASE_URL

Base = declarative_base()

def connect_db():
    engine = create_engine(DATABASE_URL, connect_args={})
    session = Session(bind=engine.connect())
    return session

class User(Base):
    __tablename__ = "users"

    id = sqlalchemy.Column(Integer, primary_key=True)
    name = sqlalchemy.Column(String)
    login = sqlalchemy.Column(String)
    password = sqlalchemy.Column(String)
    token = sqlalchemy.Column(String)
    email = sqlalchemy.Column(String)
    social = sqlalchemy.Column(String)
    location = sqlalchemy.Column(String)
    age = sqlalchemy.Column(Integer)
    hobby = sqlalchemy.Column(String)
    career = sqlalchemy.Column(String)
    education = sqlalchemy.Column(String)
    cigaretes = sqlalchemy.Column(String)
    alcohol = sqlalchemy.Column(String)
    music = sqlalchemy.Column(String)
    films = sqlalchemy.Column(String)
    videogames = sqlalchemy.Column(String)
    serials = sqlalchemy.Column(String)
    books = sqlalchemy.Column(String)
    avatar = sqlalchemy.Column(String)

class Chat(Base):
    __tablename__ = "chats"

    __table_args__ = (PrimaryKeyConstraint('id1', 'id2'),)

    id1 = sqlalchemy.Column(Integer, ForeignKey("user.id"))
    id2 = sqlalchemy.Column(Integer, ForeignKey("user.id"))
    location = sqlalchemy.Column(String)

class Shared(Base):
    __tablename__ = "shared"

    __table_args__ = (PrimaryKeyConstraint('owner_id', 'shared_id'),)

    owner_id = sqlalchemy.Column(Integer, ForeignKey("user.id"))
    shared_id = sqlalchemy.Column(Integer, ForeignKey("user.id"))
    field = sqlalchemy.Column(String)