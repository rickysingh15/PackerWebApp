from src.infrastructure.database.db_factory import get_engine_and_session
from fastapi import FastAPI
from src.adapters.controllers.user_controller import UserController
from src.adapters.routes.user_routes import get_user_routes
from src.adapters.routes.guide_routes import guide_routes
from src.adapters.repositories.postgres_user_repo import PostgresUserRepo
from src.adapters.repositories.postgres_guide_repo import PostgresGuideRepo
from src.adapters.controllers.guide_controller import GuideController
from src.config import settings
from src.infrastructure.logging.logger import get_logger
# from adapters.outbound.mongo_user_repo import MongoUserRepo

logger = get_logger(__name__)
app = FastAPI()
DATABASE_URL = f"postgresql+asyncpg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
engine, async_session = get_engine_and_session(DATABASE_URL)

# 🔄 Swap repos here: Postgres OR Mongo
user_repo = PostgresUserRepo(async_session())
guide_repo = PostgresGuideRepo(async_session())
# user_repo = MongoUserRepo()

user_controller = UserController(user_repo)
app.include_router(get_user_routes(user_controller), prefix="/api")

guide_controller = GuideController(guide_repo)
app.include_router(guide_routes(guide_controller), prefix="/api")
