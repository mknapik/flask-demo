from flask import Flask, request, jsonify
from pprint import pprint
from toolz.dicttoolz import keyfilter
from typing import NamedTuple

from .error import ApplicationError
from .config import (
    DevFlaskConfig,
    DevConfig,
    Config,
    ProductionConfig,
    ProductionFlaskConfig,
)


def build_app(config: Config):
    flask = Flask(__name__)

    flask.config.from_object(config.flask_config)

    return flask


app = build_app(ProductionConfig(ProductionFlaskConfig))
app = build_app(DevConfig(DevFlaskConfig))


@app.route("/env")
def env():
    return keyfilter(
        lambda x: x not in ("PERMANENT_SESSION_LIFETIME", "SEND_FILE_MAX_AGE_DEFAULT"),
        app.config,
    )


@app.route("/")
def hello_world():
    1 / 0
    return {"foo": "bar"}


@app.errorhandler(404)
def not_found(error):
    app.logger.warning(error)
    return {"errors": ["Not found!", str(error)]}, 404


@app.errorhandler(ApplicationError)
def not_found(error):
    app.logger.error(error)
    return {"errors": [str(error)]}, 500


@app.errorhandler(Exception)
def not_found(error):
    if not app.config["DEBUG"]:
        raise error
    app.logger.error(error)
    return {"errors": [str(error)]}, 500
