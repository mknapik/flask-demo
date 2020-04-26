from injector import singleton, inject

from funicular.database import Database
from funicular.model.user import User

from .repository import Repository


@singleton
class UserRepository(Repository[User]):
    @inject
    def __init__(self, db: Database):
        super().__init__()
        self.__db = db

    def all(self):
        return [
            User(name="Alice"),
            User(name="Bob"),
        ]
