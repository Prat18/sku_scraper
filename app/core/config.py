from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # General settings
    APP_NAME: str = "SKU SCRAPER"
    SCRAPING_LIMIT: int = 5
    SCRAPE_URL: str = "https://dentalstall.com/shop/page/{}/"
    DEBUG: bool = Field(default=False, env='DEBUG')

    # Database settings
    DATABASE_TYPE: str = 'json'
    DATABASE_CONFIG: dict = {
        "json": {
            "driver": "json",
            "path": "data.json"
        }
    }

    # CELERY settings
    CELERY_BROKER_URL: str = "redis://default:QSS0EHz9nC4qP3wNqlwmdqi9FoylnSfp@redis-19689.c12.us-east-1-4.ec2.redns.redis-cloud.com:19689"
    CELERY_RESULT_BACKEND: str = "redis://default:QSS0EHz9nC4qP3wNqlwmdqi9FoylnSfp@redis-19689.c12.us-east-1-4.ec2.redns.redis-cloud.com:19689"

    # REDIS settings
    CACHE_CONFIG: dict = {
        'host': 'redis-19689.c12.us-east-1-4.ec2.redns.redis-cloud.com',
        'port': 19689,
        'password': 'QSS0EHz9nC4qP3wNqlwmdqi9FoylnSfp'
    }

    # Other settings
    LOG_LEVEL: str = Field(default="info", env='LOG_LEVEL')

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


# Initialize settings
settings = Settings()
