from typing import Any, Never, Callable, TypeAlias, TypeVar
from sqlalchemy import insert, select, update
from sqlalchemy.orm import load_only, defer, aliased, selectin_polymorphic
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
        "SQLDBProvider":
            SQLQueryProvider(
                {
                    "user.get": lambda id: 
                        select(User)\
                        .join(Session, User.username == Session.userid, isouter=True)
                        .where(Session.id == id)\
                        .options(load_only(User.username, User.surname, User.name, User.patronymic, User.role)),
                    "user.add": lambda **kwargs:
                        insert(User).values(**kwargs).returning(User),
                    "card.get": lambda conditions: 
                        select(Card, Lecturer := aliased(User), Student := aliased(User), Lab, Subject.name)\
                        .filter_by(**conditions)\
                        .join(Lecturer, Card.lecturerid == Lecturer.username)\
                        .join(Student, Card.studentid == Student.username)\
                        .join(Lab, Lab.id == Card.labid)\
                        .join(Subject, Lab.subjectid == Subject.id)\
                        .options(defer(Lecturer.password), defer(Student.password)),
                    "card.get.all": lambda: 
                        select(Card, Lecturer := aliased(User), Student := aliased(User), Lab, Subject.name)\
                        .join(Lecturer, Card.lecturerid == Lecturer.username)\
                        .join(Student, Card.studentid == Student.username)\
                        .join(Lab, Lab.id == Card.labid)\
                        .join(Subject, Lab.subjectid == Subject.id)\
                        .options(defer(Lecturer.password), defer(Student.password)),
                    "card.add": lambda **kwargs:
                        insert(Card).values(**kwargs).returning(Card),
                    "group.user.add": lambda username, group:
                        insert(StudentToGroupPair).values(userid=username, groupname=group).returning(StudentToGroupPair),
                    "card.update": lambda id, **kwargs:
                        update(Card).values(kwargs).where(Card.id == id).returning(Card),
                    "group.get.all": lambda:
                        select(Group),
                    "user.get.by.credentials": lambda username, password:
                        select(User).filter_by(username=username, password=password),
                    "session.key.add": lambda username:
                        insert(Session).values(userid=username, isactive=True).returning(Session)
                }
            ),
        "MockProvider": MockQueryProvider()
    }

    def __init__(self) -> Never:
        raise NotImplementedError("Queries class is not intended to init")
    
    @classmethod
    def get(cls, provider: str, query: str, *args: Any, **kwargs: dict[str, Any]) -> sql.Executable | str | Any:
        return cls._queries[provider].query(query, *args, **kwargs)
