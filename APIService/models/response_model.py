from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import List, Dict
import re
import json


class RefiningResponse(BaseModel):
    response: List[str] = Field(..., description='The refined text')
    model_config = ConfigDict(
        json_schema_extra={
            "response": [
                "段落1",
                "段落2"
            ]
        }
    )

    @classmethod
    def from_raw_response(cls, raw_response: str):
        processed_response = re.sub(r'^.*?```json(.*?)```.*$', r'\1', raw_response, flags=re.DOTALL).strip()
        processed_response = processed_response.replace("\'", "\"")
        return cls.parse_raw(processed_response)
