from abc import abstractmethod, ABCMeta
from typing import Any, Never, Final

class Constructor(metaclass=ABCMeta):
    def __init__(self) -> Never:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def construct(**kwargs) -> Any:
        raise NotImplementedError

class TestPageConstructor(Constructor):
    test_page: Final[str] = """
<html>
    <head>
        <title>Some HTML in here</title>
    </head>
    <body>
        <h1>test</h1>
    </body>
</html>
"""

    def __init__(self) -> Never:
        super().__init__()

    @classmethod
    def construct(cls, **kwargs) -> str:
        return cls.test_page
