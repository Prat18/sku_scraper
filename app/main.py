from fastapi import FastAPI
from app.api.v1.endpoints import scraper

app = FastAPI()

app.include_router(scraper.router, prefix="/api/v1/scraper", tags=["bg"])
