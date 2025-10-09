
from src.domain.entities.player import Player
class User(Player):
    def __init__(self, first_name, last_name, username, email, password, phone_number):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.phone_number = phone_number