from pydantic import BaseModel

class UserLoginForm(BaseModel):
    login: str
    password: str
