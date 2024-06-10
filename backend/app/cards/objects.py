from typing import Any, Literal, Optional
from pydantic import BaseModel
from users.objects import User


class Lab(BaseModel):
    id: int
    name: str
    description: str
    semester: int
    groupname: str
    deadline: Optional[str]

class Card(BaseModel):
    studentid: str
    labid: int
    content: str
    comments: str
    lecturerid: str
    variant: Optional[int] = None
    info: dict[str, Any]

class FullCard(BaseModel):
    id: int
    student: User
    lab: Lab
    content: str
    comments: str
    variant: Optional[int] = None
    info: dict[str, Any]
    lecturer: User
    status: Literal["Accepted", "Declined", "Postponed", "Pending"]
    creationdate: str

class CreatedCard(Card):
    status: Literal["Accepted", "Declined", "Postponed", "Pending"]
    creationdate: str


