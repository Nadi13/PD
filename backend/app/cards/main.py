from typing import Any, Final, Literal, Optional, Sequence
from db import DataProvider
from containers.queries import Queries
from config import config
from icecream import ic
from .objects import *


PROVIDER: Final[str] = config["dataProvider"]

def get(id: int, provider: DataProvider) -> Optional[FullCard]:
    cards: Sequence[Sequence[dict[str, Any]]] = provider.query(Queries.get(PROVIDER, "card.get", id))
    if not cards:
        return None
    card = cards[0]
    ic(card)
    return FullCard(
        **(card[0]),
        lecturer=User(**(card[1])),
        student=User(**(card[2])),
        lab=Lab(**(card[3]))
    )

def get_all(provider: DataProvider) -> dict[str, Any]:
    cards: Sequence[Sequence[CreatedCard]] = provider.query(Queries.get(PROVIDER, "card.get.all"))
    return cards[0]

def add(id: int, studentid: str, labid: int, content: str,
        comments: str, info: Optional[dict[str, Any]],
        provider: DataProvider) -> Literal["Invalid value", "Success", "Internal error"]:
    raise NotImplementedError
