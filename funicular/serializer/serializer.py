import abc
from typing import Generic, TypeVar, Dict

Model = TypeVar("Model")


class Serializer(Generic[Model], metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def serialize(self, model: Model) -> Dict:
        pass
