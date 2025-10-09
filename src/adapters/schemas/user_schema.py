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

class ResetPasswordSchema(BaseModel):
    email: EmailStr
    old_password: str
    new_password: str

class UserUpdateSchema(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None
    phone_number: str | None = None
    email: EmailStr | None = None
    password: str | None = None