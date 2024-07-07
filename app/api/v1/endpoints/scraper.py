from fastapi import APIRouter
from app.schemas.scrape import ScraperInput
from app.core.config import settings
from task import scrape

scrape_url = settings.SCRAPE_URL
scraping_limit = settings.SCRAPING_LIMIT

router = APIRouter()


@router.post("/")
def start_scraper(scraper: ScraperInput):
    limit = min(scraping_limit, scraper.limit)
    task = scrape.apply_async((scraper.offset, limit))
    return {"task_id": task.id}


@router.get("/status/{task_id}")
def get_scraping_status(task_id: str):
    task = scrape.AsyncResult(task_id)

    if task.state == "PENDING":
        return {"status": task.state}
    elif task.state != "FAILURE":
        return {"status": task.state, "result": task.result}
    else:
        return {"status": task.state, "result": str(task.info)}
