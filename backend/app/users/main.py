from typing import Any, Hashable, Optional, TypeAlias


User: TypeAlias = dict[str, Any]

def get_user(id: Hashable) -> Optional[User]:
    # temp
    if id == "123":
        return {"name": "test", "age": 22}
    return None