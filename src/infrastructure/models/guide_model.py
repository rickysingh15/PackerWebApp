from sqlalchemy import Column, String, TIMESTAMP, text, ARRAY
from sqlalchemy.orm import declarative_base
import uuid

Base = declarative_base()

class GuideModel(Base):
    __tablename__ = "guides"

    id = Column(String, foreign_key="users.id", nullable=False, unique=True, default=lambda: str(uuid.uuid4()))
    guide_id = Column(String, primary_key=True, nullable=False, unique=True, default=lambda: str(uuid.uuid4()))
    bio = Column(String, nullable=True)
    languages = Column(ARRAY(String), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=text('now()'))