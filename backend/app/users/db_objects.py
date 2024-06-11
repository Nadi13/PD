from typing import Any, Optional
from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sql
from general import DBObject


class User(DBObject):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(sql.String(32), primary_key=True)
    password: Mapped[str] = mapped_column(sql.CHAR(64))
    surname: Mapped[str] = mapped_column(sql.Text)
    name: Mapped[str] = mapped_column(sql.Text)
    patronymic: Mapped[str] = mapped_column(sql.Text)
    role: Mapped[str] = mapped_column(sql.Text)

class Session(DBObject):
    __tablename__ = "sessions"

    id: Mapped[str] = mapped_column(sql.Uuid, primary_key=True, server_default="gen_random_uuid()")
    userid: Mapped[str] = mapped_column(sql.String(32), sql.ForeignKey("users.username"))
    isactive: Mapped[bool] = mapped_column(default=True)

class StudentToGroupPair(DBObject):
    __tablename__ = "studenttogroup"

    userid: Mapped[str] = mapped_column(sql.String(32), sql.ForeignKey("users.username"))
    groupname: Mapped[str] = mapped_column(sql.Text, sql.ForeignKey("groups.name"))

    __table_args__ = (
        sql.PrimaryKeyConstraint(
            userid,
            groupname
        ),
    )

class LecturerToLabPair(DBObject):
    __tablename__ = "lecturertolab"

    userid: Mapped[str] = mapped_column(sql.String(32), sql.ForeignKey("users.username"))
    labid: Mapped[int] = mapped_column(sql.Integer, sql.ForeignKey("labs.id"))

    __table_args__ = (
        sql.PrimaryKeyConstraint(
            userid,
            labid
        ),
    )

class Group(DBObject):
    __tablename__ = "groups"

    name: Mapped[str] = mapped_column(sql.Text, primary_key=True)
    description: Mapped[Optional[str]] = mapped_column(sql.Text, nullable=True)

#class Student(DBObject):
#    __tablename__ = "students"
#
#    username: Mapped[str] = mapped_column(sql.String(32), sql.ForeignKey("users.username"), primary_key=True)
