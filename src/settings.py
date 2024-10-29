from typing import Optional
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


class Redis(Environment):
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: Optional[SecretStr] = None


class Bot(Environment):
    TOKEN: SecretStr = SecretStr("7886604072:AAE-K1clVIuY8VEY86tIBk3z07y0gU_Q1a8")


class Settings(Bot, Redis):
    USER_ID: int = 0


settings = Settings()
