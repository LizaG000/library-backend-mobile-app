from sqlalchemy.ext.asyncio import AsyncSession
from src.usecase.base import Usecase
from uuid import UUID
from dataclasses import dataclass
from src.infra.postgres.gateways.books import GetBookByIDGate
from src.usecase.books.schemas import BookAllSchemas
from src.infra.s3.download_file import DownloadFileService

@dataclass(slots=True, frozen=True, kw_only=True)
class GetBookByIDUsecase(Usecase[UUID, BookAllSchemas]):
    session: AsyncSession
    get_book: GetBookByIDGate
    download_file: DownloadFileService
    
    async def __call__(self, book_id: UUID) -> BookAllSchemas:
        async with self.session.begin():
            book = await self.get_book(book_id)
            book.pdf =  await self.download_file.download_file(folder = "book", name = book.pdf)
            book.image =  await self.download_file.download_file(folder = "img", name = book.image)

            return book




            
