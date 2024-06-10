from datetime import datetime
from typing import Any, Literal, Optional, Sequence
from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sql
from general import DBObject


class Lab(DBObject):
    __tablename__ = "labs"

    id: Mapped[int] = mapped_column(sql.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(sql.Text)
    description: Mapped[str] = mapped_column(sql.Text)
    semester: Mapped[int] = mapped_column(sql.SmallInteger)
    groupname: Mapped[str] = mapped_column(sql.Text, sql.ForeignKey("groups.name"))
    deadline: Mapped[Optional[datetime]] = mapped_column(sql.DateTime, nullable=True)
    subjectid: Mapped[int] = mapped_column(sql.Integer, sql.ForeignKey("subjects.id"))

class Card(DBObject):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(sql.Integer, primary_key=True)
    studentid: Mapped[str] = mapped_column(sql.String(32), sql.ForeignKey("users.username"))
    labid: Mapped[int] = mapped_column(sql.Integer, sql.ForeignKey("labs.id"))
    content: Mapped[str] = mapped_column(sql.Text)
    comments: Mapped[str] = mapped_column(sql.Text)
    status: Mapped[Literal["Accepted", "Declined", "Postponed", "Pending"]] = mapped_column(sql.Text)
    creationdate: Mapped[datetime] = mapped_column(sql.DateTime)
    lecturerid: Mapped[str] = mapped_column(sql.String(32), sql.ForeignKey("users.username"))
    variant: Mapped[Optional[int]] = mapped_column(sql.SmallInteger, nullable=True)
    info: Mapped[dict[str, Any]] = mapped_column(sql.JSON, default=dict())

class Subject(DBObject):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(sql.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(sql.Text, unique=True)
    