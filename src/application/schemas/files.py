from uuid import UUID
from datetime import datetime
from src.application.schemas.common import BaseModel

class FileSchemas(BaseModel):
    id: UUID
    name: str
    book_id: UUID
    created_at: datetime
    updated_at: datetime

class CreateFileSchema(BaseModel):
    name: str
    book_id: UUID
