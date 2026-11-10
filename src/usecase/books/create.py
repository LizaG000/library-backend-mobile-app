from sqlalchemy.ext.asyncio import AsyncSession
from src.usecase.base import Usecase
from src.infra.postgres.gateways.base import CreateReturningGate, CreateGate
from src.application.schemas.books import CreateBookSchema, BookSchemas
from src.application.schemas.files import CreateFileSchema
from src.infra.postgres.tables import BookModel, ImageBookModel, FileBookModel
from dataclasses import dataclass
from src.usecase.books.schemas import CreateBookFileSchemas
from src.infra.s3.upload_file import UploadFileService

@dataclass(slots=True, frozen=True, kw_only=True)
class CreateBookUsecase(Usecase[CreateBookFileSchemas, BookSchemas]):
    session: AsyncSession
    create_book: CreateReturningGate[BookModel, CreateBookSchema, BookSchemas]
    create_img: CreateGate[ImageBookModel, CreateFileSchema]
    create_file: CreateGate[FileBookModel, CreateFileSchema]
    upload_file: UploadFileService
    
    async def __call__(self, data: CreateBookFileSchemas) -> BookSchemas:
        async with self.session.begin():
            book = await self.create_book(CreateBookSchema(
                name=data.name,
                author_first_name=data.author_first_name,
                author_last_name=data.author_last_name,
                author_middle_name=data.author_middle_name,
                year=data.year,
            ))

            await self.upload_file.upload_file(data.image, "img", str(book.id))
            await self.create_img(CreateFileSchema(
                name = str(book.id),
                book_id = book.id
            ))
            
            await self.upload_file.upload_file(data.pdf, "book", str(book.id))
            await self.create_file(CreateFileSchema(
                name = str(book.id),
                book_id = book.id
            ))
            return book




            
