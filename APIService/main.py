from fastapi import FastAPI
from APIService.routers import creating, proofreading, knowledge

app = FastAPI()

app.include_router(creating.router, prefix="/creating", tags=["creating"])
app.include_router(proofreading.router, prefix="/proofreading", tags=["proofreading"])
app.include_router(knowledge.router, prefix="/knowledge", tags=["knowledge"])

@app.get("/")
async def root():
    return {"message": "I'm working!"}


