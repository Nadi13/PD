import abc
from typing import Any, Sequence
import sqlalchemy as sql
import sqlalchemy.ext.asyncio as sqla
from icecream import ic
from fastapi.encoders import jsonable_encoder


__all__ = ["DataProvider", "SQLDBProvider"]

# Interfaces

class DataProvider(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def query(self, query: Any, *args, **kwargs) -> Any:
        raise NotImplementedError

# Implementations

class SQLDBProvider(DataProvider):
    def __init__(self) -> None:
        pass
    
    async def query(self, query: sql.Executable, *args, **kwargs) -> Sequence[dict[str, Any]]:
        session: sqla.AsyncSession = kwargs["session"]
        result: Sequence[Any] = (await session.execute(query, kwargs)).all()
        compiled_result: list[list[dict[str, Any]]] = []
        for item in result:
            compiled_result.append(list())
            for object_ in item:
                compiled_result[-1].append(*jsonable_encoder([object_]))
        return compiled_result
