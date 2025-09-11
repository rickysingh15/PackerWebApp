from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    async def save(self, user):
        pass