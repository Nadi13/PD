from string import Template
from typing import Any, Never, Callable, TypeAlias
from sqlalchemy import insert, select
from sqlalchemy.orm import load_only, defer
from users.db_objects import *
from cards.db_objects import *


QueryConstructor: TypeAlias = Callable[..., sql.Executable | str | Any]

class Queries:
    _queries: dict[str, dict[str, Callable | str | Any]] = {
        "PostgreSQLProvider": {
            "user.get": lambda id: select(User)\
                                    .join(Session, User.username == Session.userid, isouter=True)
                                    .where(Session.id == id)\
                                    .options(load_only(User.username, User.surname, User.name, User.patronymic, User.role)),

            "user.add": lambda **kwargs:
                insert(User).values(**kwargs).returning(User),
            "card.get": lambda id: select(Card, User, Lab)\
                                    .where(Card.id == id)\
                                    .join(User, User.username == Card.studentid and User.username == Lab.lecturer)\
                                    .join(Lab, Lab.id == Card.labid)\
                                    .options(defer(User.password))
        },
        "MockProvider": {
            "user.get": lambda *args: "user.get",
            "user.add": lambda *args: "user.add",
            "card.get": lambda *args: "card.get"
        }
    }

    def __init__(self) -> Never:
        raise NotImplementedError("Queries class is not intended to init")
    
    @classmethod
    def get(cls, provider: str, query: str) -> QueryConstructor | Any:
        return cls._queries[provider][query]
