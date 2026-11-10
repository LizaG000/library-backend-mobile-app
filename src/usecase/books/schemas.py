from uuid import UUID
from datetime import datetime
from fastapi import UploadFile
from src.application.schemas.common import BaseModel

class CreateBookFileSchemas(BaseModel):
    name: str
    author_first_name: str
    author_last_name: str
    author_middle_name: str
    year: int

    image: UploadFile
    pdf: UploadFile

class BookImgSchemas(BaseModel):
    id: UUID
    name: str
    author_first_name: str
    author_last_name: str
    author_middle_name: str
    year: int
    image: str
    created_at: datetime
    updated_at: datetime


class BookAllSchemas(BaseModel):
    id: UUID
    name: str
    author_first_name: str
    author_last_name: str
    author_middle_name: str
    year: int
    image: str
    pdf: str
    current_page: int|None
    created_at: datetime
    updated_at: datetime