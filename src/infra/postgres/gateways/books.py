from uuid import UUID

from src.infra.postgres.gateways.base import PostgresGateway
from src.infra.postgres.tables import BookModel, ImageBookModel, FileBookModel, ReadingProgressModel
from dataclasses import dataclass
from src.usecase.books.schemas import BookImgSchemas, BookAllSchemas
from sqlalchemy import func, select
from src.application.errors import NotFoundError




@dataclass(slots=True, kw_only=True)
class GetBookIMGGate(PostgresGateway):
    async  def __call__(self, ) -> list[BookImgSchemas]:
        stmt = (
            select(
                BookModel.id,
                BookModel.name,
                BookModel.author_first_name,
                BookModel.author_last_name,
                BookModel.author_middle_name,
                BookModel.year,
                ImageBookModel.name.label("image"),
                BookModel.created_at,
                BookModel.updated_at,
            )
            .join(BookModel, BookModel.id == ImageBookModel.book_id)
        )
        
        result = (await self.session.execute(stmt)).mappings().fetchall()
        if result is None:
            raise  NotFoundError(BookModel)
        return [BookImgSchemas.model_validate(row) for row in result]


@dataclass(slots=True, kw_only=True)
class GetBookByIDGate(PostgresGateway):

    async def __call__(self, book_id: UUID) -> BookAllSchemas:
        stmt = (
            select(
                BookModel.id,
                BookModel.name,
                BookModel.author_first_name,
                BookModel.author_last_name,
                BookModel.author_middle_name,
                BookModel.year,
                ImageBookModel.name.label("image"),
                FileBookModel.name.label("pdf"),
                ReadingProgressModel.current_page,
                BookModel.created_at,
                BookModel.updated_at,
            )
            .select_from(BookModel)
            .join(
                ImageBookModel,
                BookModel.id == ImageBookModel.book_id,
            )
            .join(
                FileBookModel,
                BookModel.id == FileBookModel.book_id,
            )
            .outerjoin(
                ReadingProgressModel,
                BookModel.id == ReadingProgressModel.book_id,
            )
            .where(BookModel.id == book_id)
        )

        result = (
            await self.session.execute(stmt)
        ).mappings().one_or_none()

        if result is None:
            raise NotFoundError(BookModel)

        return BookAllSchemas.model_validate(result)
