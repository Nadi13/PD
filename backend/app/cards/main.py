from typing import Any, Final, Literal, Optional, Sequence
from db import DataProvider
from containers.queries import Queries
from config import config
from icecream import ic
from .objects import *


PROVIDER: Final[str] = config["dataProvider"]

def get(id: int, provider: DataProvider) -> Optional[FullCard]:
    cards: Sequence[dict[str, Any]] = provider.query(Queries.get(PROVIDER, "card.get", id))
    if not cards:
        return None
    ic(cards[0])
    return FullCard(
        **(cards[0]),
        lecturer=User(**{item[0]: item[1] for item in cards[0].items()}),
        lab=Lab(**(cards[0]))
    )

def get_all(provider: DataProvider) -> dict[str, Any]:
    cards: Sequence[CreatedCard] = provider.query(Queries.get(PROVIDER, "card.get.all"))
    return cards

def add(id: int, studentid: str, labid: int, content: str,
        comments: str, info: Optional[dict[str, Any]],
        provider: DataProvider) -> Literal["Invalid value", "Success", "Internal error"]:
    raise NotImplementedError
