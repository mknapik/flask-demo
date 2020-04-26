from flask import Flask
from injector import inject

from .config import Config
from .error import ApplicationError


class AppFactory:
    @inject
    def __init__(self, config: Config):
        self.__app = self.__build_app(config)

    @property
    def app(self):
        return self.__app

    def __build_app(self, config: Config) -> Flask:
        flask = Flask(__name__)

        flask.config.from_object(config.flask_config)

        from .route.health_check import blueprint as health_check
        from .route.user import blueprint as users
        from .route.error_handler import application_error, not_found, fatal_error

        flask.register_blueprint(health_check, url_prefix="/health")
        flask.register_blueprint(users, url_prefix="/users")
        flask.register_error_handler(404, not_found)
        flask.register_error_handler(ApplicationError, application_error)
        flask.register_error_handler(Exception, fatal_error)

        return flask
