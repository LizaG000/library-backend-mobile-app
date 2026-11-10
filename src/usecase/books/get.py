from sqlalchemy.ext.asyncio import AsyncSession
from src.usecase.base import Usecase
from src.infra.postgres.gateways.books import GetBookIMGGate
from src.application.schemas.books import BookSchemas
from src.application.schemas.files import CreateFileSchema
from src.infra.postgres.tables import BookModel, ImageBookModel, FileBookModel
from dataclasses import dataclass
from src.usecase.books.schemas import BookImgSchemas
from src.infra.s3.download_file import DownloadFileService

@dataclass(slots=True, frozen=True, kw_only=True)
class GetBookUsecase(Usecase[None, list[BookImgSchemas]]):
    session: AsyncSession
    get_book: GetBookIMGGate
    download_file: DownloadFileService
    
    async def __call__(self, data: None = None) -> list[BookImgSchemas]:
        async with self.session.begin():
            books =  await self.get_book()
            for i in range(len(books)):
                books[i].image = await self.download_file.download_file(folder = "img", name = str(books[i].id))

            return books




            
