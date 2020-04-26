from flask_injector import FlaskInjector
from injector import Injector, Binder, singleton

from .app import AppFactory
from .config import (
    DevFlaskConfig,
    DevConfig,
    Config,
    FlaskConfig,
)


def configure_for_testing(binder: Binder):
    binder.bind(FlaskConfig, to=DevFlaskConfig, scope=singleton)
    binder.bind(Config, to=DevConfig, scope=singleton)


injector = Injector([configure_for_testing])
app = injector.get(AppFactory).app

FlaskInjector(app=app)
