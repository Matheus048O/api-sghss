# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str = "localhost"  # <-- TROCAR AQUI
    DB_PORT: str = "5432"
    DB_NAME: str = "sghss"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "mudar123"

    @property
    def DATABASE_URL(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"

settings = Settings()

