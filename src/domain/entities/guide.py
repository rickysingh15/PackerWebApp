from src.domain.entities.player import Player
from uuid import uuid4

class Guide(Player):
    def __init__(self):
        super().__init__()
        self.guide_id = str(uuid4())
        self.bio: str = ""
        self.languages: list[str] = []
        self.created_events: list[str] = []

    def add_language(self, language: str):
        if language not in self.languages:
            self.languages.append(language)

    def create_event(self, event: str):
        if event not in self.created_events:
            self.created_events.append(event)