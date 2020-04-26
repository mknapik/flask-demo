from pytest import fixture
from typing import List
from uuid import uuid4 as uuid
from pretend import stub, call_recorder

from expects import expect, equal, contain_exactly

from funicular.service.user import UserService
from funicular.repository.repository import Repository, Model


def describe_service():
    @fixture(scope="module")
    def user_id():
        return uuid()

    @fixture(scope="module")
    def user_repository(user_id):
        return stub(all=call_recorder(lambda: [user_id]))

    def describe_list():
        @fixture
        def subject(service):
            return service.list()

        @fixture
        def service(repository):
            return UserService(repository)

        def it_proxies_repository(user_repository):
            service = UserService(user_repository)
            expect(service.list()).to(contain_exactly(*user_repository.all()))
