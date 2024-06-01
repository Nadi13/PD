import abc
from typing import Any
from general import Disposable

__all__ = ["DataProvider", "PostgreSQLProvider"]

# Interfaces

class DataProvider(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def query(self, query: str, **kwargs) -> Any:
        raise NotImplementedError

# Implementations

class PostgreSQLProvider(DataProvider, Disposable):
    def __init__(self) -> None:
        super().__init__()
        # raise NotImplementedError
    
    def query(self, query: str, **kwargs) -> Any:
        raise NotImplementedError
    
    def dispose(self) -> None:
        try:
            self.db.close()
        except:
            pass
        self.db = None
    
    def __del__(self) -> None:
        self.dispose()

