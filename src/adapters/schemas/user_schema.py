from pydantic import BaseModel, EmailStr
from uuid import UUID

class RegisterUserSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    phone_number: str
    email: EmailStr
    password: str

class LoginUserSchema(BaseModel):
    email: EmailStr
    password: str