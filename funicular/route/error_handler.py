from flask import current_app as app, Blueprint
from funicular.logger import Logger


def not_found(error, logger: Logger):
    logger.warning(error)
    return {"errors": ["Not found!", str(error)]}, 404


def application_error(error, logger: Logger):
    logger.error(error)
    return {"errors": [str(error)]}, 500


def fatal_error(error, logger: Logger):
    if app.config["DEBUG"]:
        raise error
    logger.error(error)
    return {"errors": [str(error)]}, 500
