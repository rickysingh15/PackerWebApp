from abc import ABC, abstractmethod
from uuid import uuid4
from datetime import datetime

class Player(ABC):
    def __init__(self):
        self._id = str(uuid4())
        self._created_at = datetime.utcnow()

    @property
    def id(self):
        return self._id
    @property
    def created_at(self):
        return self._created_at

