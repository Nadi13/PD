from string import Template
from typing import Never


class Queries:
    _queries: dict[str, dict[str, Template]] = {
        "PostgreSQLProvider": {
            "user.get": Template
                ('''
                 select *
                 from sessions
                 left join users
                   on sessions.userId = users.id
                 where sessions.id = $id
                '''
                )
        }
    }

    def __init__(self) -> Never:
        raise NotImplementedError("Queries class is not intended to init")
    
    @classmethod
    def get(cls, provider: str, query: str, **kwargs) -> str:
        return cls._queries[provider][query].substitute(**kwargs)
