import logging
import os
from langchain_openai import AzureChatOpenAI
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from .routers import creating, proofreading, knowledge_base, refining
from .core.settings import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(creating.router, prefix="/creating", tags=["creating"])
app.include_router(proofreading.router, prefix="/proofreading", tags=["proofreading"])
app.include_router(knowledge_base.router, prefix="/knowledge", tags=["knowledge_base"])
app.include_router(refining.router, prefix="/refining", tags=["refining"])


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(exc: RequestValidationError):
    logger.error(f"RequestValidationError: {exc.errors()}")
    return JSONResponse(content=exc.errors(), status_code=400)


@app.get("/")
async def root():
    print(config.debug)
    return {"message": "I'm working!"}
