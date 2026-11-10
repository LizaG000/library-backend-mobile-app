from minio import Minio
from starlette.concurrency import run_in_threadpool

from src.config import MinioConfig


class DownloadFileService:
    def __init__(self, config: MinioConfig):
        self.config = config
        self.client = Minio(
            endpoint=config.endpoint,
            access_key=config.access_key,
            secret_key=config.secret_key,
            secure=config.secure,
        )

    async def download_file(self, object_name: str) -> bytes:

        def download():
            response = self.client.get_object(
                bucket_name=self.config.minio.bucket_name,
                object_name=object_name,
            )

            try:
                return response.read()
            finally:
                response.close()
                response.release_conn()

        return await run_in_threadpool(download)