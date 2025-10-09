from fastapi import HTTPException, status
from src.application.interfaces.user_repository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.infrastructure.models.guide_model import GuideModel
from src.infrastructure.logging.logger import get_logger

logger = get_logger(__name__)

class PostgresGuideRepo(UserRepository):
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def save(self, guide_entity):
        guide_model = GuideModel(
            id=guide_entity.id,
            bio=guide_entity.bio,
            languages=guide_entity.languages,
            created_events=guide_entity.created_events,
        )

        self.db_session.add(guide_model)
        await self.db_session.commit()
        await self.db_session.refresh(guide_model)
        logger.info(f"Guide saved with ID: {guide_model.id}")
        return {"status": "saved in Postgres", "guide": guide_model.__dict__}
    

    async def update(self, guide_model: GuideModel):
        await self.db_session.commit()
        await self.db_session.refresh(guide_model)
        logger.info(f"Guide updated with ID: {guide_model.id}")
        return {"status": "updated in Postgres", "guide": guide_model.__dict__}

    async def get_by_id(self, guide_id: str):
        result = await self.db_session.execute(select(GuideModel).where(GuideModel.id == guide_id))
        result = result.scalars().first()
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Guide with id {guide_id} not found")
        return result
    
    async def get_by_email(self, email: str):
        result = await self.db_session.execute(select(GuideModel).where(GuideModel.email == email))
        result = result.scalars().first()
        if result is None:
            logger.warning(f"Guide with email {email} not found")
            return None
        return result