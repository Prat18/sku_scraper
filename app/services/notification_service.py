from logger.logger import Logger

logger = Logger('scraper').get_logger()


class NotificationService:
    def __init__(self, task):
        self.task = task

    def notify(self):
        logger.info(f"{self.task.request.id} has completed scraping!")
