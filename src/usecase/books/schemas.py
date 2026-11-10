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