from src.domain.entities.user import User
import uuid
from src.infrastructure.logging.logger import get_logger

logger = get_logger(__name__)


class ResetPasswordUseCase:
    def __init__(self, user_repo, password_hasher=None):
        self.user_repo = user_repo
        self.password_hasher = password_hasher

    async def execute(self, email, new_password):
        user = await self.user_repo.get_by_email(email)
        if user is None:
            logger.warning(f"Login failed for email {email}: user not found.")
            return {"status": "error", "message": "Invalid email or password."}

        hashed_password = self.password_hasher.hash(new_password)
        user.password = hashed_password

        await self.user_repo.update(user)
        logger.info(f"Password reset successful for user {email}")
        return {"message": "Password reset successful"}