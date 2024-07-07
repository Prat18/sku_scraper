import logging
import os
from logging.handlers import RotatingFileHandler


class Logger:
    def __init__(self, name, log_file='C:/Users/praty/custom/sku_scraper/app.log', level=logging.INFO, max_bytes=1024 * 1024, backup_count=3):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Create handlers
        self.file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

        self.console_handler = logging.StreamHandler()
        self.console_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.console_handler)

    def get_logger(self):
        return self.logger


# Example of how to use the Logger class
if __name__ == '__main__':
    log = Logger('exampleLogger').get_logger()
    log.info('This is an info message')
    log.warning('This is a warning message')
    log.error('This is an error message')
