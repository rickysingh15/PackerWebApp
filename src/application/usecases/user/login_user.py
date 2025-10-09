from src.domain.entities.user import User
import uuid
from src.infrastructure.logging.logger import get_logger

logger = get_logger(__name__)

class LoginUserUseCase():

    def __init__(self, user_repo, password_hasher=None):
        self.user_repo = user_repo
        self.password_hasher = password_hasher

    async def execute(self, email, password):
        user = await self.user_repo.get_by_email(email)
        if user is None:
            logger.warning(f"Login failed for email {email}: user not found.")
            return {"status": "error", "message": "Invalid email or password."}

        if self.password_hasher and not self.password_hasher.verify(password, user.password):
            logger.warning(f"Login failed for email {email}: incorrect password.")
            return {"status": "error", "message": "Invalid email or password."}

        logger.info(f"User with email {email} logged in successfully.")
        return {"status": "success", "message": "Login successful.", "user": user.__dict__}