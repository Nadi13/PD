from typing import Any
from abc import ABCMeta, abstractmethod


class Disposable(metaclass=ABCMeta):
    '''
    Objects that use external resources that need to be closed
    when they are no longer in use.
    '''
    @abstractmethod
    def dispose() -> None:
        raise NotImplementedError
