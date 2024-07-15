from pydantic import BaseModel, Field


class RefiningRequest(BaseModel):
    text: str = Field(..., description='The text to be refined')
    style: str = Field(..., description='The style of the text to be refined')
