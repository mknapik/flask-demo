from injector import inject
from .simple import Foo


class Nestee:
    @inject
    def __init__(self, foo: Foo):
        self.test = "test"


class Bar:
    @inject
    def __init__(self):
        pass

    @inject
    def asd(self, nestee: Nestee) -> str:
        return nestee.test
