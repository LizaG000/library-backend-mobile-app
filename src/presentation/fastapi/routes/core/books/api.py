from dishka.integrations.fastapi import DishkaRoute
from dishka.integrations.fastapi import FromDishka
from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, File, Form, UploadFile
from fastapi import status
from src.application.schemas.books import BookSchemas
from src.usecase.books.schemas import CreateBookFileSchemas
from src.presentation.fastapi.routes.core.books.schemas import RequestCreateBookFileSchemas
from src.usecase.books.create import CreateBookUsecase
from src.usecase.books.get import GetBookUsecase
from src.usecase.books.get_by_id import GetBookByIDUsecase
from src.usecase.books.schemas import BookImgSchemas, BookAllSchemas
ROUTER = APIRouter(route_class=DishkaRoute)

@ROUTER.post('', status_code=status.HTTP_200_OK)
async def create_book(
    usecase: FromDishka[CreateBookUsecase],
    data: Annotated[str, Form()],
    image: Annotated[UploadFile, File()],
    pdf: Annotated[UploadFile, File()]) -> BookSchemas:
    book_data = RequestCreateBookFileSchemas.model_validate_json(data)
    return await usecase(CreateBookFileSchemas(
        name = book_data.name,
        author_first_name = book_data.author_first_name,
        author_last_name = book_data.author_last_name,
        author_middle_name = book_data.author_middle_name,
        year = book_data.year,
        image = image,
        pdf = pdf
    ))

@ROUTER.get('', status_code=status.HTTP_200_OK)
async def get_book(
    usecase: FromDishka[GetBookUsecase]) -> list[BookImgSchemas]:
    return await usecase()


@ROUTER.get('/id', status_code=status.HTTP_200_OK)
async def get_book_by_id(
    usecase: FromDishka[GetBookByIDUsecase],
    book_id: UUID) -> BookAllSchemas:
    return await usecase(book_id)