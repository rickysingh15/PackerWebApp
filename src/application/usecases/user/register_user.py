from src.domain.entities.user import User
import uuid
from src.infrastructure.logging.logger import get_logger

logger = get_logger(__name__)


class RegisterUserUseCase:
    def __init__(self, user_repo, password_hasher=None):
        self.user_repo = user_repo
        self.password_hasher = password_hasher

    async def execute(self, first_name, last_name, username, email, password, phone_number):

        existing_user = await self.user_repo.get_by_email(email)  # Check if user with email already exists
        if existing_user is not None:
            logger.warning(f"User with email {email} already exists.")
            return {"status": "error", "message": "User with this email already exists."}

        if self.password_hasher:
            hashed_password = self.password_hasher.hash(password)

        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=hashed_password if self.password_hasher else password,
            phone_number=phone_number
        )
        return await self.user_repo.save(user)