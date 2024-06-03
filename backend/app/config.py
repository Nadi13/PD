import json
from typing import Any, Final


def __get_config() -> dict[str, Any]:
    with open("./config.json") as file:
        return json.load(file)

config: Final[dict[str, Any]] = __get_config()
