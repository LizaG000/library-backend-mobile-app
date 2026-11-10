from dishka import make_async_container
from src.main.provider import MainProvider
from src.infra.postgres.provider import PostgresProvider
from src.infra.s3.provider import MinioProvider
from src.config import Config
from src.main.config import config

container = make_async_container(
    MainProvider(),
    PostgresProvider(),
    MinioProvider(),
    context={
        Config: config
    }
)