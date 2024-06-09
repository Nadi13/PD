import abc
from typing import Any, Callable, Sequence
from general import Disposable
import sqlalchemy as sql
import sqlalchemy.orm as orm
from icecream import ic
from fastapi.encoders import jsonable_encoder
from general import DBObject


__all__ = ["DataProvider", "SQLDBProvider", "PostgreSQLProvider"]

# Interfaces

class DataProvider(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def query(self, query: Any, *args, **kwargs) -> Any:
        raise NotImplementedError

# Implementations

class SQLDBProvider(DataProvider, Disposable):
    def __init__(self, engine: str) -> None:
        super().__init__()
        self.engine = sql.create_engine(engine, echo=True)
        self.db = self.engine.connect()
    
    def query(self, query: sql.Executable, *args, **kwargs) -> Sequence[dict[str, Any]]:
        with orm.Session(self.engine) as session:
            result: Sequence[Any] = session.execute(query, kwargs).all()
            ic(result)
            compiled_result: list[list[dict[str, Any]]] = []
            for item in result:
                compiled_result.append(list())
                for object_ in item:
                    compiled_result[-1].append(*jsonable_encoder([object_]))
            ic(compiled_result)
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
    _queries: dict[str, list[dict]] = {
        "user.get": [
            {
                "username": "test5642",
                "patronymic": "testovich",
                "surname": "test",
                "name": "tes1",
                "role": "human"
            }
        ],
        "user.add": [{"success": True}],
        "card.get": [
            {
                "id": 1,
                "studentid": "asdq1",
                "lab": {
                    "id": 1,
                    "name": "Лабораторная работа 1",
                    "description": "Установить .NET 7 и запустить Hello World.",
                    "semester": 3,
                    "groupname": "Individual_1",
                    "deadline": "2024-06-06T20:25:29.262096"
                },
                "content": "",
                "comments": "",
                "variant": None,
                "info": {},
                "lecturer": {
                    "surname": "test",
                    "name": "Лабораторная работа 1",
                    "patronymic": "testovich",
                    "username": "test5642",
                    "role": "human"
                },
                "status": "Pending",
                "creationdate": "2024-06-06T02:16:52.634746"
            }
        ],
        "cards.get.all": [
            {
                "id": 1,
                "studentid": "asdq1",
                "labid": 1,
                "content": "",
                "comments": "",
                "lecturerid": "test5642",
                "variant": None,
                "info": dict(),
                "status": "Pending",
                "creationdate": "2024-06-06T02:16:52.634746"
            },
            {
                "id": 23,
                "studentid": "asdqasd1",
                "labid": 3,
                "content": "Аовылаыр",
                "comments": "Обратите внимание на MethodName",
                "lecturerid": "test5642",
                "variant": 2,
                "info": dict(),
                "status": "Declined",
                "creationdate": "2024-08-06T02:16:52.634746"
            }
        ]
    }

    def query(self, query: str, *args, **kwargs) -> list[dict]:
        return self._queries[query]
