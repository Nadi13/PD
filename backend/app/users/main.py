from typing import Any, Hashable, Optional, TypeAlias
from db import DataProvider
from containers.queries import Queries


User: TypeAlias = dict[str, Any]

def get_user(id: Hashable, provider: DataProvider) -> Optional[User]:
    user: dict[str, Any] = provider.query(Queries.get("user.get"))
    return user