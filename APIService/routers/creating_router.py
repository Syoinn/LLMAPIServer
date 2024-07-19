from fastapi import APIRouter, HTTPException
# from app.services.creation_service import create_text

router = APIRouter()

@router.post("/create")
async def create(input_text: str):
    try:
        # result = create_text(input_text)
        return {}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
