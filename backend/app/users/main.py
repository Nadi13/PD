from typing import Any, Final, Hashable, Literal, Optional, Sequence, TypeAlias
from db import DataProvider
from containers.queries import Queries
from hashlib import sha256
from config import config
from icecream import ic
from .objects import *


ROLES: Final[list[str]] = config["roles"].copy()
PROVIDER: Final[str] = config["dataProvider"]

def get(id: str, provider: DataProvider) -> Optional[User]:
    if not (id and id.isalnum()):
        return None
    users: Sequence[dict[str, Any]] = provider.query(Queries.get(PROVIDER, "user.get", id))
    if not users:
        return None
    return User(**users[0][0])

def _validate_username(username: str) -> bool:
    return 4 < len(username) < 33 and username.isprintable()

def _validate_password(password: str) -> bool:
    return 6 < len(password) < 128 and password.isprintable()

def _validate_user(info: UserWithCredentials) -> bool:
    for value in ["surname", "name", "patronymic"]:
        if not vars(info)[value].isalpha():
            return False
    if info.role not in ROLES:
        return False
    return True

def add(user: UserWithCredentials, provider: DataProvider) -> Literal["Invalid value", "Success", "Internal error"]:
    if not (_validate_username(user.username) and _validate_password(user.password) and _validate_user(user)):
        return "Invalid value"
    
    isSuccessful: bool = provider.query(
        Queries.get(
            PROVIDER,
            "user.add",
            username=user.username,
            password=sha256(user.password.encode()).hexdigest(),
            **user.model_dump(exclude=["username", "password"])
        )
    )
    return "Success" if isSuccessful else "Internal error"
