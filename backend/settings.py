from pydantic import BaseSettings


class Settings(BaseSettings):
    db_uri: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
