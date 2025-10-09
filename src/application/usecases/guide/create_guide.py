

from src.domain.entities.guide import Guide
from src.infrastructure.logging.logger import get_logger

logger = get_logger(__name__)

class CreateGuideUseCase:
    def __init__(self, guide_repo):
        self.guide_repo = guide_repo

    async def execute(self, bio, languages):
        guide = Guide(
            bio=bio,
            languages=languages
        )
        return await self.guide_repo.save(guide)