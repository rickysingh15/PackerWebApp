from fastapi import HTTPException, status
from src.application.interfaces.user_repository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.infrastructure.models.user_model import UserModel
from src.infrastructure.logging.logger import get_logger

logger = get_logger(__name__)

class PostgresUserRepo(UserRepository):
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def save(self, user_entity):
        user_model = UserModel(
            id=user_entity.id,
            first_name=user_entity.first_name,
            last_name=user_entity.last_name,
            username=user_entity.username,
            phone_number=user_entity.phone_number,
            email=user_entity.email,
            password=user_entity.password
        )
        self.db_session.add(user_model)
        await self.db_session.commit()
        await self.db_session.refresh(user_model)
        logger.info(f"User saved with ID: {user_model.id}")
        return {"status": "saved in Postgres", "user": user_model.__dict__}
    

    async def update(self, user_model: UserModel):
        await self.db_session.commit()
        await self.db_session.refresh(user_model)
        logger.info(f"User updated with ID: {user_model.id}")
        return {"status": "updated in Postgres", "user": user_model.__dict__}

    async def get_by_id(self, user_id: str):
        result = await self.db_session.execute(select(UserModel).where(UserModel.id == user_id))
        result = result.scalars().first()
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
        return result
    
    async def get_by_email(self, email: str):
        result = await self.db_session.execute(select(UserModel).where(UserModel.email == email))
        result = result.scalars().first()
        if result is None:
            logger.warning(f"User with email {email} not found")
            return None
        return result