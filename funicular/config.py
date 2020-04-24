import abc
from typing import NamedTuple
from injector import inject


class FlaskConfig(NamedTuple):
    DEBUG: bool
    TESTING: bool


DevFlaskConfig = lambda: FlaskConfig(DEBUG=True, TESTING=True)
ProductionFlaskConfig = lambda: FlaskConfig(DEBUG=False, TESTING=False)


class Config(object):
    @inject
    def __init__(self, flask_config: FlaskConfig):
        self.flask_config = flask_config

    @property
    def DATABASE_URI() -> str:
        return "sqlite:///:memory:"

    @property
    @abc.abstractmethod
    def FEATURE_ENABLED() -> bool:
        pass


class DevConfig(Config):
    @property
    def FEATURE_ENABLED(self):
        return True


class ProductionConfig(Config):
    @property
    def FEATURE_ENABLED(self):
        return True
