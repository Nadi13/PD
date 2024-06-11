from typing import Any, Final, Literal, Optional, Sequence
from db import DataProvider
from containers.queries import Queries
from config import config
from icecream import ic
from .objects import *
from sqlalchemy.ext.asyncio import AsyncSession


PROVIDER: Final[str] = config["dataProvider"]

async def get(id: int, session: AsyncSession, provider: DataProvider) -> Optional[FullCard]:
    cards: Sequence[Sequence[dict[str, Any]]] = await provider.query(Queries.get(PROVIDER, "card.get", id), session=session)
    if not cards:
        return None
    card = cards[0]
    return FullCard(
        **(card[0]),
        lecturer=User(**(card[1])),
        student=User(**(card[2])),
        lab=Lab(**(card[3])),
        subject=card[4]
    )

async def get_all(provider: DataProvider, session: AsyncSession) -> Sequence[FullCard]:
    cards: Sequence[Sequence[CreatedCard]] = await provider.query(Queries.get(PROVIDER, "card.get.all"), session=session)
    return [
        FullCard(
            **(card[0]),
            lecturer=User(**(card[1])),
            student=User(**(card[2])),
            lab=Lab(**(card[3])),
            subject=card[4]
        )
        for card in cards
    ]

async def add(card: Card, session: AsyncSession, provider: DataProvider) -> Literal["Invalid value", "Success", "Internal error"]:
    await provider.query(Queries.get(PROVIDER, "card.add"), **card.model_dump(), session=session, status="Pending")
    await session.commit()
    return "Success"

async def update(card: CardUpdate, session: AsyncSession, provider: DataProvider) -> Literal["Invalid value", "Success", "Internal error"]:
    await provider.query(Queries.get(PROVIDER, "card.update", card.id, **card.model_dump(exclude_none=True, exclude=["id"])), session=session)
    await session.commit()
    return "Success"
