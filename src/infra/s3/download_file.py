
from datetime import timedelta

from minio import Minio
from starlette.concurrency import run_in_threadpool

from src.config import MinioConfig


class DownloadFileService:
    def __init__(self, config: MinioConfig, client: Minio):
        self.config = config
        self.client = client

    async def download_file(
        self,
        folder: str,
        name: str,
    ) -> str:
        object_name = f"{folder}/{name}"

        def get_url():
            return self.client.presigned_get_object(
                bucket_name=self.config.bucket_name,
                object_name=object_name,
                expires=timedelta(hours=1),
            )

        return await run_in_threadpool(get_url)
