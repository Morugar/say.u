from fastapi import APIRouter, Body, Depends
from forms import UserLoginForm
from models import connect_db

router = APIRouter()

@router.post('/login', name="user:login")
def login(user_form: UserLoginForm, databasse=(Depends(connect_db))):
    return user_form.email and user_form.password

