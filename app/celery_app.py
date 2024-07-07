# app/celery_app.py
from celery import Celery
from app.core.config import settings

CELERY_BROKER_URL = settings.CELERY_BROKER_URL
CELERY_RESULT_BACKEND = settings.CELERY_RESULT_BACKEND

celery_app = Celery(
    "sku_scraper",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

celery_app.conf.update(imports=['task'])
celery_app.conf.update(task_serializer="json", accept_content=["json"], result_serializer="json")
