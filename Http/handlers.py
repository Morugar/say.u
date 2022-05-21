from datetime import datetime
import io
import uuid

import ftplib

from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status

from Http.forms import UserLoginForm, UserRegisterForm, ShareUserForm, PatchUserForm, ChatCreateForm, SendForm, token
from Http.models import connect_db, User, Shared, Chat  # UserPatch

router = APIRouter()


def alls(database=Depends(connect_db)):
    users = database.query(User).all()
    return users


@router.get('/all')
def alle(database=Depends(connect_db)):
    users = database.query(User).all()
    return users


@router.post('/auth', name="user:login")
def login(user: UserLoginForm, database=Depends(connect_db)):
    user_exist = database.query(User).filter(User.login == user.login).one_or_none()
    if not user_exist:
        return {
            "error": {
                "code": 401,
                "message": "Unauthorized",
                "errors": {
                    "user": "User with this login not exist"
                }
            }
        }
    elif user_exist.password != user.password:
        return {
            "error": {
                "code": 401,
                "message": "Unauthorized",
                "errors": {
                    "password": "Password is incorrect"
                }
            }
        }
    token = user_exist.token
    return {
            'code': 200,
            'token': token
    }


@router.put('/changeProfile', name='user:edit')
def change_user(form: PatchUserForm, database=Depends(connect_db)):
    user = database.query(User).filter(User.token == form.token).one_or_none()
    users = database.query(User).all()

    user = users[user.id - 1]
    user.name = form.name
    user.login = form.login
    user.email = form.email
    user.social = form.social
    user.location = form.location
    user.age = form.age
    user.hobby = form.hobby
    user.career = form.career
    user.education = form.education
    user.cigaretes = form.cigaretes
    user.alcohol = form.alcohol
    user.music = form.music
    user.films = form.films
    user.videogames = form.videogames
    user.serials = form.serials
    user.books = form.books
    user.avatar = form.avatar
    database.add(user)
    database.commit()

    return {"1": form.name, "2": form.login, "3": form.age, "4": form.cigaretes}


@router.post('/chat', name='chat:create')
def create_chat(chat: ChatCreateForm, database=Depends(connect_db)):
    user1 = database.query(User.id).filter(User.id == chat.id1).one_or_none()
    user2 = database.query(User.id).filter(User.id == chat.id2).one_or_none()
    ftp = ftplib.FTP()
    host = "localhost"
    port = 21
    user = "moruga"
    ftp.connect(host, port)
    ftp.login(user)
    data = ftp.retrlines('LIST')
    if (str(user1.id) + "-" + str(user2.id) + ".txt") in ftp.nlst():
        print("rofl")
        return {"error"}
    nul = io.BytesIO(b'')
    file = ftp.storlines('STOR ' + str(user1.id) + "-" + str(user2.id) + ".txt", nul)
    return data

@router.post('/send', name='chat:send')
def send(chat: SendForm, database=Depends(connect_db)):
    user1 = database.query(User.id).filter(User.id == chat.id1).one_or_none()
    user2 = database.query(User.id).filter(User.id == chat.id2).one_or_none()
    sender = database.query(User.id).filter(User.id == chat.sender_id).one_or_none()
    ftp = ftplib.FTP()
    host = "localhost"
    port = 21
    user = "moruga"
    ftp.connect(host, port)
    ftp.login(user)
    data = ftp.retrlines('LIST')
    if str(user1.id) + "-" + str(user2.id) + ".txt" not in ftp.nlst():
        return {"error"}
    mess = str(sender.id) + "/" + str(datetime.now().day) + "." + str(datetime.now().month) + "." + str(datetime.now().year) + "/" + chat.message
    bytes = str.encode(mess)
    IO = io.BytesIO(bytes)
    file = ftp.storlines('APPE ' + str(user1.id) + "-" + str(user2.id) + ".txt", IO)
    return file


@router.post('/register', name='user:create')
def create_user(user: UserRegisterForm, database=Depends(connect_db)):
    exists_user = database.query(User.id).filter(User.email == user.email and User.login == user.login).first()

    if exists_user:
        return {
            'error': {
                'code': 422,
                'message': "User with this login or email already exist"
            }
        }

    new_user = User(
        login=user.login,
        password=user.password,
        email=user.email,
        name=user.name,
        token=str(uuid.uuid4())
    )

    database.add(new_user)
    database.flush()
    database.commit()
    return {
        'data': {
            'code': 204,
            'message': "User successfuly created"
        }
    }


@router.post('/share')
def share(user: ShareUserForm, database=Depends(connect_db)):
    fields = ["name", "email", "age", "hobby", "social", "location", "career", "education", "cigaretes", "alcohol",
              "music", "films", "videogames", "serials", "books"]

    owner = database.query(User).filter(User.id == user.owner_id).one_or_none()

    if not owner:
        return {
            "error": {
                "code": 422,
                "message": "Validation error",
                "errors": {
                    "owner": "Owner of field is not exist"
                }
            }
        }

    if user.owner_id == user.shared_id:
        return {
            "error": {
                "code": 422,
                "message": "Validation error",
                "errors": {
                    "id": "You can't share field with yourself"
                }
            }
        }

    friend = database.query(User).filter(User.id == user.shared_id).one_or_none()

    if not friend:
        return {
            "error": {
                "code": 422,
                "message": "Validation error",
                "errors": {
                    "shared": "Sharing person is not exist"
                }
            }
        }

    if owner.token != user.token:
        return {
            "error": {
                "code": 401,
                "message": "Authorized",
                "errors": {
                    "token": "Auth token is invalide or not belong to owner"
                }
            }
        }

    if user.field not in fields:
        return {
            "error": {
                "code": 422,
                "message": "Validation error",
                "errors": {
                    "field": "Unsupported field to share"
                }
            }
        }

    table = database.query(Shared).filter(
        Shared.owner_id == user.owner_id and Shared.shared_id == user.shared_id and Shared.field == user.field).one_or_none()
    if table:
        return {
            "error": {
                "code": 422,
                "message": "Validation error",
                "errors": {
                    "field": "This field was already shared"
                }
            }
        }

    new_sharing = Shared(
        owner_id=user.owner_id,
        shared_id=user.shared_id,
        field=user.field
    )

    database.add(new_sharing)
    database.flush()
    database.commit()
    return {
        "data": {
            "owner_id": new_sharing.owner_id,
            "shared_id": new_sharing.shared_id,
            "field": new_sharing.field
        }
    }

@router.post('/info')
def get(token: token, database=Depends(connect_db)):
    user = database.query(User).filter(User.token == token.token).one_or_none()
    return user