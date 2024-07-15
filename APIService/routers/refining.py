from fastapi import APIRouter, HTTPException
from typing import List, Dict
from ..models.request_model import RefiningRequest
from ..llm.refining_service import refining
from pydantic import ValidationError

router = APIRouter()

FUNC_LIST = ["polish", "expand", "shorten", "continue", "inspiration"]


@router.post("/{func}")
async def text_enhancement(func: str, request: RefiningRequest) -> Dict[str, List[str]]:
    if func not in FUNC_LIST:
        raise HTTPException(status_code=400, detail="Invalid function name")
    try:
        response = await refining(text=request.text, style=request.style)
        return response
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
