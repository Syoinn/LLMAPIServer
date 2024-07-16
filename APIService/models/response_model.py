from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import List, Dict


class RefiningResponse(BaseModel):
    response: Dict[str, List[str]] = Field(..., description='The refined text')
    model_config = ConfigDict(
        json_schema_extra={
            "response": [
                "段落1",
                "段落2"
            ]
        }
    )

