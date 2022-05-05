from fastapi import APIRouter, Body, Depends
from forms import UserLoginForm
from models import connect_db, User, Chat, Shared

router = APIRouter()

@router.post('/login', name="user:login")
def login(user_form: UserLoginForm, database=(Depends(connect_db))):
    user = database.query(User).filter(User.login == user_form.login).one_or_none()
    if not user or user.password != user_form.password:
        return {'error': 'Error'}
    token = user.token
    return token

