import uuid
from datetime import datetime
from sqlalchemy import UUID
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import ForeignKey
from typing import Annotated

uuid_pk = Annotated[uuid.UUID, mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        default=uuid.uuid4,
    )]

created_at = Annotated[datetime, mapped_column(
    DateTime(timezone=True),
    default=func.now(), 
    nullable=False,

)]
updated_at = Annotated[datetime, mapped_column(
    DateTime(timezone=True),
    default=func.now(), 
    nullable=False,

)]

class BaseDBModel(DeclarativeBase):
    __tablename__: str
    __table_args__: dict[str, str] | tuple = {'schema': 'db_schema'}

    @classmethod
    def group_by_fields(cls, exclude: list[str] | None = None) -> list:
        payload = []
        if not exclude:
            exclude = []

        for column in cls.__table__.columns:
            if column.key in exclude:
                continue

            payload.append(column)

        return payload

class BookModel(BaseDBModel):
    __tablename__ = 'books'
    id: Mapped[uuid_pk]
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    author_first_name: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )
    author_last_name: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )
    author_middle_name: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )
    year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

class ImageBookModel(BaseDBModel):
    __tablename__ = 'image_books'
    id: Mapped[uuid_pk]
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    book_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("db_schema.books.id"),
        nullable=False,
        unique=True,
    )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

class FileBookModel(BaseDBModel):
    __tablename__ = 'file_books'
    id: Mapped[uuid_pk]
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    book_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("db_schema.books.id"),
        nullable=False,
        unique=True,
    )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class ReadingProgressModel(BaseDBModel):
    __tablename__ = 'reading_progress'
    id: Mapped[uuid_pk]
    book_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("db_schema.books.id"),
        nullable=False,
        unique=True,
    )

    current_page: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
    )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

