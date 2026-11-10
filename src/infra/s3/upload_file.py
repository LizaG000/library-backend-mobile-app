
import uuid

from fastapi import UploadFile
from minio import Minio
from starlette.concurrency import run_in_threadpool

from src.config import MinioConfig


class UploadFileService:
    def __init__(self, config: MinioConfig, client: Minio):
        self.config = config
        self.client = client

    async def upload_file(
        self,
        file: UploadFile,
        folder: str,
        filename: str,
    ) -> str:
        object_name = f"{folder}/{uuid.uuid4()}_{filename}"

        await file.seek(0)

        def upload():
            self.client.put_object(
                bucket_name=self.config.bucket_name,
                object_name=object_name,
                data=file.file,
                length=-1,
                part_size=10 * 1024 * 1024,
                content_type=file.content_type or "application/octet-stream",
            )

        await run_in_threadpool(upload)

        return object_name
