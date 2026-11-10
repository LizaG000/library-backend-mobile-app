from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from src.presentation.fastapi.routes.core.users.api import ROUTER as USER_ROUTER
from src.presentation.fastapi.routes.core.books.api import ROUTER as BOOK_ROUTER
from src.presentation.fastapi.routes.core.progress.api import ROUTER as PROGRESS_ROUTER

def setup_core_router() -> APIRouter:
    router = APIRouter(route_class=DishkaRoute)

    router.include_router(prefix='/user', router=USER_ROUTER)
    router.include_router(prefix='/book', router=BOOK_ROUTER)
    router.include_router(prefix='/progress', router=PROGRESS_ROUTER)
    return router
