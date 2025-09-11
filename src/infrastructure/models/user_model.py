from sqlalchemy import Column, String, TIMESTAMP, text
from sqlalchemy.orm import declarative_base
import uuid

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=True, unique=True)  # optional, unique if provided
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=text('now()'))