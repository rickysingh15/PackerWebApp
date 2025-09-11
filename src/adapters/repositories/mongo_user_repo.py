from src.application.interfaces.user_repository import UserRepository

class MongoUserRepo(UserRepository):
    async def save(self, user):
        # Here you'd use Motor (Mongo async client)
        return {"status": "saved in MongoDB", "user": user.__dict__}