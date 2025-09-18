from src.application.usecases.register_user import RegisterUserUseCase
from src.application.usecases.login_user import LoginUserUseCase
from src.adapters.schemas.user_schema import RegisterUserSchema, LoginUserSchema
from src.infrastructure.security.password_hasher import PasswordHasher

class UserController:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    async def register_user(self, user_data: RegisterUserSchema):
        usecase = RegisterUserUseCase(self.user_repo, password_hasher=PasswordHasher())
        return await usecase.execute(user_data.model_dump())
    
    async def login_user(self, user_data: LoginUserSchema):
        usecase = LoginUserUseCase(self.user_repo, password_hasher=PasswordHasher())
        return await usecase.execute(**user_data)