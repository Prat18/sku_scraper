# database_factory.py

from app.db.json_database import JSONDatabase
from app.core.config import settings

DATABASE_CONFIG = settings.DATABASE_CONFIG


class DatabaseFactory:
    @staticmethod
    def create_database(config_name):
        config = DATABASE_CONFIG.get(config_name)
        if not config:
            raise ValueError(f"Invalid database configuration: {config_name}")

        driver_type = config.get("driver")
        if driver_type == "sqlite":
            pass
        elif driver_type == "mysql":
            pass
        elif driver_type == "json":
            return JSONDatabase(config.get("path"))
        else:
            raise ValueError(f"Unsupported database driver: {driver_type}")
