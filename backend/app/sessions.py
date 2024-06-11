from general import Disposable
import sqlalchemy.ext.asyncio as sqla
from typing import AsyncIterator
from icecream import ic
from contextlib import asynccontextmanager


class SessionManager(Disposable):
    def __init__(self, login: str, password: str, location: str, database: str) -> None:
        self._engine: sqla.AsyncEngine = sqla.create_async_engine(f"postgresql+asyncpg://{login}:{password}@{location}/{database}", echo=True)
        self._sessionmaker = sqla.async_sessionmaker(autocommit=False, bind=self._engine)
    
    async def connect(self) -> AsyncIterator[sqla.AsyncConnection]:
        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception as e:
                ic("Exception:", e)
                await connection.rollback()
                raise
    
    @asynccontextmanager
    async def session(self) -> AsyncIterator[sqla.AsyncSession]:
        session = self._sessionmaker()
        try:
            yield session
        except Exception as e:
            ic("Exception", e)
            await session.rollback()
            raise
        finally:
            await session.close()
    
    async def with_session(self) -> AsyncIterator[sqla.AsyncSession]:
        async with self.session() as session:
            yield session
    
    async def dispose(self) -> None:
        await self._engine.dispose()
        self._engine = None
        self._sessionmaker = None
