from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String

class Base(DeclarativeBase):
    pass

class ApplicationModel(Base):
    __tablename__ = 'application'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    brief_info: Mapped[str]
    room_numb: Mapped[int]
    quest_name: Mapped[str]
    service: Mapped[str]