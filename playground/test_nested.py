from injector import Injector
from pytest import raises

from .nested import Bar, Nestee


def test_nested():
    i = Injector()
    bar: Bar = i.get(Bar)
    with raises(TypeError):
        bar.asd()
    assert i.call_with_injection(bar.asd) == "test"
