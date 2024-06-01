from typing import Any
from abc import ABCMeta, abstractmethod


def get_config() -> dict[str, Any]:
    return dict() # temp

class Disposable(metaclass=ABCMeta):
    @abstractmethod
    def dispose() -> None:
        raise NotImplementedError
