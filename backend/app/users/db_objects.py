from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sql
from general import DBObject


class User(DBObject):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(sql.String(32), primary_key=True)
    password: Mapped[str] = mapped_column(sql.String(64))
    surname: Mapped[str] = mapped_column(sql.Text)
    name: Mapped[str] = mapped_column(sql.Text)
    patronymic: Mapped[str] = mapped_column(sql.Text)
    role: Mapped[str] = mapped_column(sql.Text)

class Session(DBObject):
    __tablename__ = "sessions"

    id: Mapped[str] = mapped_column(sql.CHAR(64), primary_key=True)
    userid: Mapped[str] = mapped_column(sql.String(32), sql.ForeignKey("users.username"))
    isactive: Mapped[bool] = mapped_column(default=True)
