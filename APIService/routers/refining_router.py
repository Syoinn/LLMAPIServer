import logging
from fastapi import APIRouter, HTTPException
from typing import List, Dict
from ..models.request_model import RefiningRequest
from APIService.services.refining_service import refining
from pydantic import ValidationError

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/{func}")
async def text_enhancement(func: str, request: RefiningRequest) -> Dict[str, List[str]]:
    try:
        response = await refining(text=request.text, style=request.style, func=func)
        return response
    except ValidationError as e:
        logger.error(f"Refining error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        logger.error(f"Refining error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Refining error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
