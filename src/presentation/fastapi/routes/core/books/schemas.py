from uuid import UUID
from datetime import datetime
from fastapi import UploadFile
from src.application.schemas.common import BaseModel

class RequestCreateBookFileSchemas(BaseModel):
    name: str
    author_first_name: str
    author_last_name: str
    author_middle_name: str
    year: int
