import os
from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


class Settings(BaseSettings):
    DEBUG: bool = os.getenv("DEBUG", False)
    ZHIPU_API_KEY: str = os.getenv("ZHIPUAI_API_KEY")
    AZURE_OPENAI_API_KEY: str = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT")

    class Config:
        env_file = ".env"


@lru_cache(maxsize=1)
def get_config() -> Settings:
    return Settings()
