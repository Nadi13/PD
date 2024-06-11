import json
from typing import Any, Final
from icecream import ic


def __get_config() -> dict[str, Any]:
    config: dict[str, Any]
    with open("./config.json") as file:
        config = json.load(file)
    try:
        with open("./secrets.json") as file:
            config["secrets"] = json.load(file)
    except FileNotFoundError:
        config["secrets"] = dict()
    return config


config: Final[dict[str, Any]] = __get_config()
