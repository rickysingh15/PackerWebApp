from application.usecases.guide.create_guide import CreateGuideUseCase
from src.adapters.schemas.guide_schema import CreateGuideSchema

class GuideController:
    def __init__(self, guide_repo):
        self.guide_repo = guide_repo

    async def create_guide(self, guide_data: CreateGuideSchema):
        usecase = CreateGuideUseCase(self.guide_repo)
        return await usecase.execute(**guide_data.model_dump())
    
