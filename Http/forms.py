import email
from numpy import str_
from pydantic import BaseModel
from typing import Optional

class token(BaseModel):
    token: str

class UserLoginForm(BaseModel):
    login: str
    password: str

class UserRegisterForm(BaseModel):
    login: str
    email: str
    name: str
    password: str

class ChatCreateForm(BaseModel):
    id1: int
    id2: int

class SendForm(BaseModel):
    sender_id: int
    id1: int
    id2: int
    message: str


class ShareUserForm(BaseModel):
    owner_id: str
    shared_id: str
    token: str
    field: str

class PatchUserForm(BaseModel):
    token: str | None = None
    name: str | None = None
    login: str | None = None
    email: str | None = None
    social: str | None = None
    location: str | None = None
    age: str | None = None
    hobby: str | None = None
    career: str | None = None
    education: str | None = None
    cigaretes: str | None = None
    alcohol: str | None = None
    music: str | None = None
    films: str | None = None
    videogames: str | None = None
    serials: str | None = None
    books: str | None = None
    avatar: str | None = None