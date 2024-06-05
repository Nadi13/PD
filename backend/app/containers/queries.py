from string import Template
from typing import Any, Never, Callable, TypeAlias
from sqlalchemy import insert, select
from sqlalchemy.orm import load_only
from users.db_objects import *


QueryConstructor: TypeAlias = Callable[..., sql.Executable]

class Queries:
    _queries: dict[str, dict[str, Callable | str | Any]] = {
        "PostgreSQLProvider": {
            "user.get": lambda id: select(User)\
                                    .join(Session, User.username == Session.userid, isouter=True)
                                    .where(Session.id == id)\
                                    .options(load_only(User.surname, User.name, User.patronymic, User.role)),

            "user.add": lambda :
                insert(User).returning(User)
        },
        "MockProvider": {
            "user.get": lambda *args: "user.get",
            "user.add": lambda *args: "user.add"
        }
    }

    def __init__(self) -> Never:
        raise NotImplementedError("Queries class is not intended to init")
    
    @classmethod
    def get(cls, provider: str, query: str) -> QueryConstructor | Any:
        return cls._queries[provider][query]
