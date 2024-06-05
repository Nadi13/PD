import abc
from typing import Any, Callable, Sequence
from general import Disposable
import sqlalchemy as sql
import sqlalchemy.orm as orm
from icecream import ic
from fastapi.encoders import jsonable_encoder

__all__ = ["DataProvider", "SQLDBProvider", "PostgreSQLProvider"]

# Interfaces

class DataProvider(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def query(self, query: Any, **kwargs) -> Any:
        raise NotImplementedError

# Implementations

class SQLDBProvider(DataProvider, Disposable):
    def __init__(self, engine: str) -> None:
        super().__init__()
        self.engine = sql.create_engine(engine, echo=True)
        self.db = self.engine.connect()
    
    def query(self, query: sql.Executable, **kwargs) -> dict[str, Any]:
        with orm.Session(self.engine) as session:
            result: Sequence[Any] = session.execute(query, kwargs).all()
            compiled_result = dict()
            for item in result[0]:
                compiled_result.update(*jsonable_encoder([item]))
            session.commit()
        return compiled_result
    
    def dispose(self) -> None:
        try:
            self.db.close()
        except (NameError, AttributeError):
            pass
        self.db = None
    
    def __del__(self) -> None:
        self.dispose()

class PostgreSQLProvider(SQLDBProvider):
    def __init__(self, login: str, password: str, location: str, database: str) -> None:
        super().__init__(f"postgresql://{login}:{password}@{location}/{database}")

class MockProvider(DataProvider):
    '''Data provider for debugging without actual db'''
    _queries: dict[str, dict] = {
        "user.get": {
            "username": "test5642",
            "patronymic": "testovich",
            "surname": "test",
            "name": "tes1",
            "role": "human"
        },
        "user.add": {"success": True},
        "card.get": {
            "id": 1,
            "content": "",
            "status": "Pending",
            "info": {},
            "comments": "",
            "studentid": "asdq1",
            "labid": 1,
            "creationdate": "2024-06-06T02:16:52.634746",
            "surname": "asdf",
            "name": "Лабораторная работа 1",
            "username": "asdq1",
            "role": "student",
            "patronymic": "asdas",
            "groupname": "Individual_1",
            "lecturer": "test5642",
            "description": "Установить .NET 7 и запустить Hello World."
        }
        #"user.get": [{
        #    "name": "Юдинцева Надежда Ивановна",
        #    "number": "МО-211/2",
        #    "work": "3",
        #    "course": "3 курс, 2 сем",
        #    "date": "пт, 1 апр., 16:34",
        #    "deadline": "true"
        #},
        #{
        #    "name": "Филякин Артем Дмитриевич",
        #    "number": "МО-211/2",
        #    "work": "2",
        #    "course": "3 курс, 2 сем",
        #    "date": "пт, 3 фев., 13:40",
        #    "deadline": "true"
        #},
        #{
        #    "name": "Савченко София Дмитриевна",
        #    "number": "ФИТ-211/2",
        #    "work": "3",
        #    "course": "3 курс, 2 сем",
        #    "date": "пт, 13 фев., 22:43"
        #},
        #{
        #    "name": "Аникина Софья Дмитриевна",
        #    "number": "МО-211/1",
        #    "work": "5",
        #    "course": "3 курс, 2 сем",
        #    "date": "пт, 14 апр., 19:14"
        #}
        #],
        #"user.add": [{"success": True}]
    }

    def query(self, query: str, **kwargs) -> Any:
        return self._queries[query]
