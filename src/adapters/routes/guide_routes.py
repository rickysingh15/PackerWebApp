from fastapi import APIRouter, Depends
from adapters.schemas.user_schema import RegisterUserSchema
from src.adapters.controllers.guide_controller import GuideController
from src.adapters.schemas.guide_schema import CreateGuideSchema
from src.infrastructure.logging.logger import get_logger    

logger = get_logger(__name__)

def guide_routes(guide_controller: GuideController):
    router = APIRouter("guide", tags=["Guides"])

    @router.post("/create")
    async def create_guide(guide: CreateGuideSchema):
        return await guide_controller.create_guide(guide)


    return router