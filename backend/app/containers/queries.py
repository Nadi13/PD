from typing import Any, Never, Callable, TypeAlias, TypeVar
from sqlalchemy import insert, select
from sqlalchemy.orm import load_only, defer
from users.db_objects import *
from cards.db_objects import *
from db import DataProvider
from icecream import ic


T = TypeVar("T")
QueryConstructor: TypeAlias = Callable[..., sql.Executable | str | Any]

class SQLQueryProvider(DataProvider):
    def __init__(self, store: dict[str, QueryConstructor]) -> None:
        self.store = store

    def query(self, query: str, *args, **kwargs) -> sql.Executable:
        return self.store[query](*args, **kwargs)

class MockQueryProvider(DataProvider):
    def query(self, query: T, **kwargs) -> T:
        return query

class Queries:
    _queries: dict[str, DataProvider] = {
        "PostgreSQLProvider":
            SQLQueryProvider(
                {
                    "user.get": lambda id: 
                        select(User)\
                        .join(Session, User.username == Session.userid, isouter=True)
                        .where(Session.id == id)\
                        .options(load_only(User.username, User.surname, User.name, User.patronymic, User.role)),
                    "user.add": lambda **kwargs:
                        insert(User).values(**kwargs).returning(User),
                    "card.get": lambda id: 
                        select(Card, User, Lab)\
                        .where(Card.id == id)\
                        .join(User, User.username == Card.lecturerid)\
                        .join(Lab, Lab.id == Card.labid)\
                        .options(defer(User.password)),
                    "card.get.all": lambda: select(Card)
                }
            ),
        "MockProvider": MockQueryProvider()
    }

    def __init__(self) -> Never:
        raise NotImplementedError("Queries class is not intended to init")
    
    @classmethod
    def get(cls, provider: str, query: str, *args: Any, **kwargs: dict[str, Any]) -> sql.Executable | str | Any:
        return cls._queries[provider].query(query, *args, **kwargs)
