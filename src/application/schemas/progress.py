from uuid import UUID
from datetime import datetime
from src.application.schemas.common import BaseModel

class ProgressSchemas(BaseModel):
    id: UUID
    book_id: UUID
    current_page: int
    created_at: datetime
    updated_at: datetime

class CreateProgressSchema(BaseModel):
    book_id: UUID
    current_page: int

class UpdateProgressSchema(BaseModel):
    book_id: UUID
    current_page: int
