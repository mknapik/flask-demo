import abc
from typing import List, Generic, TypeVar

Model = TypeVar("Model")


class Repository(Generic[Model], metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def all(self) -> List[Model]:
        pass
