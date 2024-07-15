import os
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug: bool = Field(True, env='DEBUG')


config = Settings()
