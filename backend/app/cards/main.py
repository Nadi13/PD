from typing import Any, Final, Optional, Sequence
from db import DataProvider
from containers.queries import Queries
from config import config
from icecream import ic
from general import DBObject
from fastapi.encoders import jsonable_encoder


PROVIDER: Final[str] = config["dataProvider"]

def get(id: int, provider: DataProvider) -> Optional[dict[str, Any]]:
    cards: Sequence[dict[str, Any]] = provider.query(Queries.get(PROVIDER, "card.get")(id))
    if not cards:
        return None
    return cards[0]

def get_all(provider: DataProvider) -> dict[str, Any]:
    cards: dict[str, Any] = provider.query(Queries.get(PROVIDER, "card.get.all")())
    return cards
