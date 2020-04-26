from flask import Blueprint, current_app as app
from toolz.dicttoolz import keyfilter

from funicular.database import Database
from funicular.logger import Logger

blueprint = Blueprint("routes", __name__)


@blueprint.route("/env")
def env():
    return keyfilter(
        lambda x: x not in ("PERMANENT_SESSION_LIFETIME", "SEND_FILE_MAX_AGE_DEFAULT"),
        app.config,
    )


@blueprint.route("/db")
def database(db: Database, logger: Logger):
    logger.info("hello world")
    return {"db": db.check()}


@blueprint.route("/error")
def error():
    return 1 / 0


__all__ = [blueprint]
