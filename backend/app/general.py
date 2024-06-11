from typing import Any
from abc import ABCMeta, abstractmethod
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel


class Disposable(metaclass=ABCMeta):
    '''
    Objects that use external resources that need to be closed
    when they are no longer in use.
    '''
    @abstractmethod
    def dispose() -> None:
        raise NotImplementedError

class DBObject(DeclarativeBase):
    pass
