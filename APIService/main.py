from fastapi import FastAPI
from APIService.routers import creating, proofreading, knowledge_base
from APIService.core.config import config


app = FastAPI()

app.include_router(creating.router, prefix="/creating", tags=["creating"])
app.include_router(proofreading.router, prefix="/proofreading", tags=["proofreading"])
app.include_router(knowledge_base.router, prefix="/knowledge", tags=["knowledge"])

@app.get("/")
async def root():
    print(config.debug)
    return {"message": "I'm working!"}


