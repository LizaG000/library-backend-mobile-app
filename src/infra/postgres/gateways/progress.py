
from dataclasses import dataclass

from sqlalchemy import update
from sqlalchemy.exc import SQLAlchemyError

from src.infra.postgres.gateways.base import PostgresGateway
from src.infra.postgres.tables import ReadingProgressModel
from src.application.schemas.progress import (
    ProgressSchemas,
    UpdateProgressSchema,
)
from src.application.errors import DatabaseUpdateError, NotFoundError


@dataclass(slots=True, kw_only=True)
class UpdateProgressGate(PostgresGateway):

    async def __call__(
        self,
        data: UpdateProgressSchema,
    ) -> ProgressSchemas:

        stmt = (
            update(ReadingProgressModel)
            .where(ReadingProgressModel.book_id == data.book_id)
            .values(current_page=data.current_page)
            .returning(ReadingProgressModel)
        )

        try:
            result = await self.session.execute(stmt)
            progress = result.scalar_one_or_none()
            
            return ProgressSchemas.model_validate(progress, from_attributes=True)

        except SQLAlchemyError as exc:
            raise DatabaseUpdateError(ReadingProgressModel) from exc


