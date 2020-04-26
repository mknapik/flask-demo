import abc
from injector import inject


class FlaskConfig(object):
    DEBUG: bool
    TESTING: bool

    def __init__(self):
        pass


class DevFlaskConfig(FlaskConfig):
    def __init__(self):
        super().__init__()
        self.DEBUG: bool = True
        self.TESTING: bool = True


class ProductionFlaskConfig(FlaskConfig):
    def __init__(self):
        super().__init__()
        self.DEBUG: bool = False
        self.TESTING: bool = False


class Config(object):
    @inject
    def __init__(self, flask_config: FlaskConfig):
        self.flask_config = flask_config

    # noinspection PyPep8Naming
    @property
    def DATABASE_URI(self) -> str:
        return "sqlite:///:memory:"

    # noinspection PyPep8Naming
    @property
    @abc.abstractmethod
    def FEATURE_ENABLED(self) -> bool:
        pass


class DevConfig(Config):
    @property
    def FEATURE_ENABLED(self):
        return True


class ProductionConfig(Config):
    @property
    def FEATURE_ENABLED(self):
        return True
