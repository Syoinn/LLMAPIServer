import logging
import os
from langchain_openai import AzureChatOpenAI
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from requests import Request

from .routers import creating_router, proofreading_router, knowledge_base_router, refining_router
from .core.settings import get_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config = get_config()

app = FastAPI()

app.include_router(creating_router.router, prefix="/creating", tags=["creating"])
app.include_router(proofreading_router.router, prefix="/proofreading", tags=["proofreading"])
app.include_router(knowledge_base_router.router, prefix="/knowledge", tags=["knowledge_base"])
app.include_router(refining_router.router, prefix="/refining", tags=["refining"])


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"RequestValidationError: {exc.errors()}")
    return JSONResponse(content=exc.errors(), status_code=400)


@app.get("/")
async def root():
    print(config.debug)
    return {"message": "I'm working!"}
