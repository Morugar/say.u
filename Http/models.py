import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, PrimaryKeyConstraint
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

    # children = relationship("Shared")

    id = sqlalchemy.Column(Integer, primary_key=True, nullable=True)
    token = sqlalchemy.Column(String, nullable=True)
    password = sqlalchemy.Column(String, nullable=True)
    name = sqlalchemy.Column(String, nullable=True)
    login = sqlalchemy.Column(String, nullable=True)
    email = sqlalchemy.Column(String, nullable=True)
    social = sqlalchemy.Column(String, nullable=True)
    location = sqlalchemy.Column(String, nullable=True)
    age = sqlalchemy.Column(Integer, nullable=True)
    hobby = sqlalchemy.Column(String, nullable=True)
    career = sqlalchemy.Column(String, nullable=True)
    education = sqlalchemy.Column(String, nullable=True)
    cigaretes = sqlalchemy.Column(String, nullable=True)
    alcohol = sqlalchemy.Column(String, nullable=True)
    music = sqlalchemy.Column(String, nullable=True)
    films = sqlalchemy.Column(String, nullable=True)
    videogames = sqlalchemy.Column(String, nullable=True)
    serials = sqlalchemy.Column(String, nullable=True)
    books = sqlalchemy.Column(String, nullable=True)
    avatar = sqlalchemy.Column(String, nullable=True)

# class UserPatch(Base):
#     __tablename__ = "users"
#
#     name = sqlalchemy.Column(String, nullable=True)
#     login = sqlalchemy.Column(String, nullable=True)
#     email = sqlalchemy.Column(String, nullable=True)
#     social = sqlalchemy.Column(String, nullable=True)
#     location = sqlalchemy.Column(String, nullable=True)
#     age = sqlalchemy.Column(Integer, nullable=True)
#     hobby = sqlalchemy.Column(String, nullable=True)
#     career = sqlalchemy.Column(String, nullable=True)
#     education = sqlalchemy.Column(String, nullable=True)
#     cigaretes = sqlalchemy.Column(String, nullable=True)
#     alcohol = sqlalchemy.Column(String, nullable=True)
#     music = sqlalchemy.Column(String, nullable=True)
#     films = sqlalchemy.Column(String, nullable=True)
#     videogames = sqlalchemy.Column(String, nullable=True)
#     serials = sqlalchemy.Column(String, nullable=True)
#     books = sqlalchemy.Column(String, nullable=True)
#     avatar = sqlalchemy.Column(String, nullable=True)

class Chat(Base):
    __tablename__ = "chats"

    __table_args__ = (PrimaryKeyConstraint('id1', 'id2'),)

    id1 = sqlalchemy.Column(Integer, ForeignKey(User.id))
    id2 = sqlalchemy.Column(Integer, ForeignKey(User.id))
    location = sqlalchemy.Column(String)

class Shared(Base):
    __tablename__ = "shared"

    __table_args__ = (PrimaryKeyConstraint('owner_id', 'shared_id'),)

    owner_id = sqlalchemy.Column(Integer, ForeignKey(User.id))
    shared_id = sqlalchemy.Column(Integer, ForeignKey(User.id))
    field = sqlalchemy.Column(String)