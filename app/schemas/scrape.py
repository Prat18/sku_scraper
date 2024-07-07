from pydantic import BaseModel
from app.core.config import settings

scraping_limit = settings.SCRAPING_LIMIT


class ScraperInput(BaseModel):
    limit: int = scraping_limit
    offset: int = 0
