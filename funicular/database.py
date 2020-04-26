from injector import inject, singleton

from .config import Config


@singleton
class Database:
    @inject
    def __init__(self, config: Config):
        self.__uri = config.DATABASE_URI

    def check(self):
        return True
