from sqlalchemy.ext.asyncio import AsyncSession
from src.usecase.base import Usecase
from src.infra.postgres.gateways.progress import UpdateProgressGate
from src.application.schemas.progress import UpdateProgressSchema, ProgressSchemas
from dataclasses import dataclass

@dataclass(slots=True, frozen=True, kw_only=True)
class UpdateProgressUsecase(Usecase[UpdateProgressSchema, ProgressSchemas]):
    session: AsyncSession
    create_progress: UpdateProgressGate
    
    async def __call__(self, data: UpdateProgressSchema) -> ProgressSchemas:
        pass
        async with self.session.begin():
            return await self.create_progress(data)
