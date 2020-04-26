from injector import singleton
from typing import Dict

from funicular.model.user import User
from funicular.serializer.serializer import Serializer


@singleton
class UserSerializer(Serializer):
    def serialize(self, user: User) -> Dict:
        return {"id": str(user.id), "type": "users", "attributes": {"name": user.name}}
