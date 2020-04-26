from flask import Flask, Response
from flask.testing import FlaskClient
from flask_injector import FlaskInjector
from injector import singleton, Binder
from pytest import fixture
from pretend import call_recorder, stub, call

from expects import expect, equal, contain_exactly, have_property

from funicular.model.user import User
from funicular.repository.user import UserRepository
from funicular.route.user import blueprint as user
from funicular.serializer.user import UserSerializer


def describe_route_user():
    @fixture
    def user_repository(users):
        return stub(all=call_recorder(lambda: users))

    @fixture
    def app(user_repository):
        flask = Flask(__name__)
        flask.register_blueprint(user)

        # insert stub at any level you wish
        def configuration(binder: Binder):
            binder.bind(UserRepository, to=user_repository, scope=singleton)

        FlaskInjector(app=flask, modules=[configuration])
        return flask

    @fixture
    def client(app) -> FlaskClient:
        with app.test_client() as client:
            yield client

    def describe_index():
        @fixture
        def user():
            return User(name="test")

        @fixture
        def users(user: User):
            return [user]

        def it_returns_all_users(client: FlaskClient, user, user_repository):
            r: Response = client.get("/")

            expect(r).to(have_property("status_code", 200))
            expect(r).to(have_property("json"))
            # use explicit expect
            expect(r.json).to(
                contain_exactly(
                    {
                        "id": str(user.id),
                        "type": "users",
                        "attributes": {"name": user.name,},
                    }
                )
            )
            # or use unmocked dependencies
            expect(r.json).to(contain_exactly(UserSerializer().serialize(user)))
            expect(user_repository.all.calls).to(
                contain_exactly(call())
            )  # probably pointless
