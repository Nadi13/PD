import string
from typing import Any, Final, Literal, Optional, Sequence
from db import DataProvider
from containers.queries import Queries
from hashlib import sha256
from config import config
from .objects import *
from sqlalchemy.ext.asyncio import AsyncSession


ROLES: Final[list[str]] = config["roles"].copy()
PROVIDER: Final[str] = config["dataProvider"]
ALLOWED_CHARS: Final[set[str]] = set(string.ascii_lowercase + string.digits + "-")

def _validate_session_key(key: str) -> bool:
    return ALLOWED_CHARS.issuperset(set(key))

async def get(id: str, session: AsyncSession, provider: DataProvider) -> Optional[User]:
    if not (id and _validate_session_key(id)):
        return None
    users: Sequence[dict[str, Any]] = await provider.query(Queries.get(PROVIDER, "user.get", id), session=session)
    if not users:
        return None
    return User(**users[0][0])

def _validate_username(username: str) -> bool:
    return 4 < len(username) < 33 and username.isprintable()

def _validate_password(password: str) -> bool:
    return 6 < len(password) < 128 and password.isprintable()

def _validate_user(user: RegistrationEntity) -> bool:
    for value in ["surname", "name", "patronymic"]:
        if not vars(user)[value].isalpha():
            return False
    if user.role not in ROLES:
        return False
    return True

def _validate_role(user: RegistrationEntity) -> bool:
    if user.role == "student":
        try:
            return user.info.get("group") != None
        except AttributeError:
            return False
    return True

async def get_by_credentials(credentials: UserCredentials, session: AsyncSession, provider: DataProvider) -> Literal["Invalid value", "Success", "Internal error", "Nonexistent value"]:
    if not (_validate_username(credentials.username) and _validate_password(credentials.password)):
        return "Invalid value"
    response = await provider.query(
        Queries.get(
            PROVIDER,
            "user.get.by.credentials",
            username=credentials.username,
            password=sha256(credentials.password.encode()).hexdigest()
        ),
        session=session
    )
    if not response:
        return "Nonexistent value"
    return "Success"

async def add(user: RegistrationEntity, session: AsyncSession, provider: DataProvider) -> Literal["Invalid value", "Success", "Internal error"]:
    if not (_validate_username(user.username) and _validate_password(user.password) and _validate_user(user) and _validate_role(user)):
        return "Invalid value"
    
    if user.role == "student":
        user = StudentWithCredentials(**user.model_dump(), group=user.info["group"])
    await provider.query(
        Queries.get(
            PROVIDER,
            "user.add",
            username=user.username,
            password=sha256(user.password.encode()).hexdigest(),
            **user.model_dump(exclude=["username", "password", "group"])
        ),
        session=session
    )
    if isinstance(user, StudentWithCredentials):
        await provider.query(
            Queries.get(
                PROVIDER,
                "group.user.add",
                username=user.username,
                group=user.group
            ),
            session=session
        )
    await session.commit()
    return "Success"

async def get_all_groups(session: AsyncSession, provider: DataProvider) -> Sequence[Group]:
    groups = await provider.query(
        Queries.get(
            PROVIDER,
            "group.get.all"
        ),
        session=session
    )
    return [Group(**item[0]) for item in groups]

async def get_new_session(user: UserCredentials, db_session: AsyncSession, provider: DataProvider) -> SessionKey:
    response = await provider.query(
        Queries.get(
            PROVIDER,
            "session.key.add",
            username=user.username
        ),
        session=db_session
    )
    await db_session.commit()
    return SessionKey(sessionKey=response[0][0]["id"])
