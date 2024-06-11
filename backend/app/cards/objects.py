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

class CardQuery(BaseModel):
    id: Optional[int] = None
    studentid: Optional[str] = None
    labid: Optional[int] = None
    content: Optional[str] = None
    comments: Optional[str] = None
    lecturerid: Optional[str] = None

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
    subject: str

class CreatedCard(Card):
    status: Literal["Accepted", "Declined", "Postponed", "Pending"]
    creationdate: str

class CardUpdate(BaseModel):
    id: int
    content: Optional[str] = None
    comments: Optional[str] = None
    status: Literal["Accepted", "Declined", "Postponed", "Pending"] | None = None
