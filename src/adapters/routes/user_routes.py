from fastapi import APIRouter, Depends
from src.adapters.controllers.user_controller import UserController
from src.adapters.schemas.user_schema import RegisterUserSchema
from src.infrastructure.logging.logger import get_logger

logger = get_logger(__name__)

def get_user_routes(user_controller: UserController):
    router = APIRouter()

    @router.post("/register")
    async def register_user(user: RegisterUserSchema):
        return await user_controller.register_user(user)

    return router