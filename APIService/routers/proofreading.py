from fastapi import APIRouter, HTTPException
# from APIService.services.proofreading_service import proofread_text

router = APIRouter()

@router.post("/proofread")
async def proofread(input_text: str):
    try:

        return {}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
