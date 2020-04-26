from typing import NamedTuple
from uuid import UUID


class User(NamedTuple):
    name: str
    id: UUID = None
