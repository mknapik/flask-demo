from dataclasses import dataclass
from typing import Optional
from uuid import UUID, uuid4


@dataclass
class User:
    name: str
    id: UUID

    def __init__(self, name: str, id: Optional[UUID] = None):
        self.name = name
        self.id = id or uuid4()
