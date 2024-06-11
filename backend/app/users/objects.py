from typing import Any, Literal, Optional
from pydantic import BaseModel


class Person(BaseModel):
    surname: str
    name: str
    patronymic: str

class UserCredentials(BaseModel):
    username: str
    password: str

class User(Person):
    username: str
    role: str

class ExtendedEntity(BaseModel):
    info: Optional[dict[str, Any]] = None

class UserWithCredentials(User, UserCredentials):
    pass

class RegistrationEntity(UserWithCredentials, ExtendedEntity):
    pass

class StudentWithCredentials(UserWithCredentials):
    role: Literal["student"]
    group: str

class Group(BaseModel):
    name: str
    description: Optional[str]

class SessionKey(BaseModel):
    sessionKey: str
