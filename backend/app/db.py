import abc
from typing import Any, Callable, Sequence
from general import Disposable
import sqlalchemy as sql
import sqlalchemy.orm as orm

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
    
    def query(self, query: sql.Executable, **kwargs) -> Sequence[Any]:
        with orm.Session(self.engine) as session:
            result = session.scalars(query, kwargs).all()
            session.commit()
        return result
    
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
