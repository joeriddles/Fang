from pydantic import (
    BaseSettings,
    PostgresDsn,
)


class Settings(BaseSettings):
    db_uri: PostgresDsn

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
