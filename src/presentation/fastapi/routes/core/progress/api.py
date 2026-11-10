from dishka.integrations.fastapi import DishkaRoute
from dishka.integrations.fastapi import FromDishka
from fastapi import APIRouter
from fastapi import status
from src.application.schemas.progress import ProgressSchemas, CreateProgressSchema, UpdateProgressSchema
from src.usecase.progress.create import CreateProgressUsecase
from src.usecase.progress.update import UpdateProgressUsecase
ROUTER = APIRouter(route_class=DishkaRoute)

@ROUTER.post('', status_code=status.HTTP_200_OK)
async def create_progress(
    usecase: FromDishka[CreateProgressUsecase],
    data: CreateProgressSchema) -> ProgressSchemas:
    return await usecase(data)

@ROUTER.patch('', status_code=status.HTTP_200_OK)
async def update_progress(
    usecase: FromDishka[UpdateProgressUsecase],
    data: UpdateProgressSchema) -> ProgressSchemas:
    return await usecase(data)
