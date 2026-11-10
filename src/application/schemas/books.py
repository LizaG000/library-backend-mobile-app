from uuid import UUID
from datetime import datetime
from src.application.schemas.common import BaseModel

class BookSchemas(BaseModel):
    id: UUID
    name: str
    author_first_name: str
    author_last_name: str
    author_middle_name: str
    year: int
    created_at: datetime
    updated_at: datetime

class CreateBookSchema(BaseModel):
    name: str
    author_first_name: str
    author_last_name: str
    author_middle_name: str
    year: int
