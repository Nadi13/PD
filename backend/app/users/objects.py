from pydantic import BaseModel


class Person(BaseModel):
    surname: str
    name: str
    patronymic: str

class UserCredentials(BaseModel):
    username: str
    password: str

class User(Person):
    username: str
    role: str

class UserWithCredentials(User, UserCredentials):
    password: str
