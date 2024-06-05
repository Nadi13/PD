from typing import Any, Final, Hashable, Literal, Optional, TypeAlias
from db import DataProvider
from containers.queries import Queries
from hashlib import sha256
from config import config
from icecream import ic
from general import DBObject


User: TypeAlias = dict[str, Any]

ROLES: Final[list[str]] = config["roles"].copy()
PROVIDER: Final[str] = config["dataProvider"]

def get(id: str, provider: DataProvider) -> Optional[User]:
    if not (id and id.isalnum()):
        return None
    user: dict[str, Any] = provider.query(Queries.get(PROVIDER, "user.get")(id))[0]
    return user

def _validate_username(username: str) -> bool:
    return 4 < len(username) < 33 and username.isprintable()

def _validate_password(password: str) -> bool:
    return 6 < len(password) < 128 and password.isprintable()

def _validate_user(info: User) -> bool:
    for value in ["surname", "name", "patronymic"]:
        if not(info.get(value) and info[value].isalpha()):
            return False
    if info.get("role") not in ROLES:
        return False
    return True

def add(username: str, password: str, info: User, provider: DataProvider) -> Literal["Invalid value", "Success", "Internal error"]:
    if not (_validate_username(username) and _validate_password(password) and _validate_user(info)):
        return "Invalid value"
    
    isSuccessful: bool = provider.query(
        Queries.get(
            PROVIDER,
            "user.add",
        )(),
        username=username,
        password=password,
        **info
    )
    return "Success" if isSuccessful else "Internal error"
