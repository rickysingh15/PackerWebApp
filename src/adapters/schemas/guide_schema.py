from pydantic import BaseModel, EmailStr
from uuid import UUID

class CreateGuideSchema(BaseModel):
    bio: str
    languages: list[str]