from typing import List

from injector import singleton, inject

from funicular.model.user import User
from funicular.repository.user import UserRepository


@singleton
class UserService:
    @inject
    def __init__(self, repository: UserRepository):
        super().__init__()
        self.__repository = repository

    def list(self) -> List[User]:
        return self.__repository.all()
