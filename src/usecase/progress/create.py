from sqlalchemy.ext.asyncio import AsyncSession
from src.usecase.base import Usecase
from src.infra.postgres.gateways.base import CreateReturningGate
from src.infra.postgres.tables import ReadingProgressModel
from src.application.schemas.progress import CreateProgressSchema, ProgressSchemas
from dataclasses import dataclass

@dataclass(slots=True, frozen=True, kw_only=True)
class CreateProgressUsecase(Usecase[CreateProgressSchema, ProgressSchemas]):
    session: AsyncSession
    create_progress: CreateReturningGate[ReadingProgressModel, CreateProgressSchema, ProgressSchemas]
    
    async def __call__(self, data: CreateProgressSchema) -> ProgressSchemas:
        pass
        async with self.session.begin():
            return await self.create_progress(data)
