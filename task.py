# app/task.py
from app.celery_app import celery_app
from app.services.scraper_service import ScraperService
from app.core.config import settings
from services.notification_service import NotificationService

scrape_url = settings.SCRAPE_URL


@celery_app.task(bind=True)
def scrape(self, offset, limit):
    scraper_service = ScraperService(scrape_url, offset, limit)
    scraper_service.scrape_sku()
    notification_service = NotificationService(self)
    notification_service.notify()
