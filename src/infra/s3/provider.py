
from dishka import Provider, Scope, provide
from minio import Minio

from src.config import MinioConfig
from src.infra.s3.upload_file import UploadFileService
from src.infra.s3.download_file import DownloadFileService


class MinioProvider(Provider):
    scope = Scope.APP

    @provide
    def get_minio_client(self, config: MinioConfig) -> Minio:
        return Minio(
            endpoint=config.endpoint,
            access_key=config.access_key,
            secret_key=config.secret_key,
            secure=config.secure,
        )

    @provide
    def get_upload_file_service(
        self,
        client: Minio,
        config: MinioConfig,
    ) -> UploadFileService:
        return UploadFileService(
            config=config,
            client=client,
        )

    @provide
    def get_download_file_service(
        self,
        client: Minio,
        config: MinioConfig,
    ) -> DownloadFileService:
        return DownloadFileService(
            client=client,
            config=config,
        )
