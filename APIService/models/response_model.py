from pydantic import BaseModel, Field, field_validator
from typing import List, Dict


class RefiningResponse(BaseModel):
    response: Dict[str, List[str]] = Field(..., description='The refined text')

