from abc import ABC, abstractmethod
from uuid import uuid4
class Event(ABC):
    def __init__(self, title, description):
        self._id = str(uuid4())
        self.title = title
        self.description = description
    @property
    def id(self):   
        return self._id
    
class TravelEvent(Event):
    def __init__(self, title, description, location, date):
        super().__init__(title, description)
        self.location = location
        self.date = date