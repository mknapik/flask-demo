from flask import Blueprint, jsonify
from toolz.curried import pipe, map

from funicular.serializer.user import UserSerializer
from funicular.service.user import UserService

blueprint = Blueprint("users", __name__)


@blueprint.route("/")
def index(service: UserService, serializer: UserSerializer):
    return pipe(service.list(), map(serializer.serialize), list, jsonify)


__all__ = [blueprint]
