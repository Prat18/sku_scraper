from time import sleep

import requests
from bs4 import BeautifulSoup
from app.cache.redis import RedisCache

from app.models.sku import SKU
from app.logger.logger import Logger
from core.config import settings
from db.database_factory import DatabaseFactory

logger = Logger('scraper').get_logger()
cache = RedisCache()

DATABASE_TYPE = settings.DATABASE_TYPE


class ScraperService:

    def __init__(self, url, offset, limit):
        self.url = url
        self.offset = offset
        self.limit = limit

    def __fetch_html_content__(self, offset, limit):
        for page_no in range(offset, limit + offset + 1):
            logger.info(f"scraping url: {self.url.format(page_no)}")
            response = requests.get(self.url.format(page_no))

            attempt = 1
            html_content = None

            while response.status_code is not 200 and attempt <= 5:
                response = requests.get(self.url.format(page_no))
                attempt = attempt + 1
                sleep(10)

            if response.status_code == 200:
                logger.info("scraping successful!")
                html_content = response.text
            else:
                logger.error(f"Failed to retrieve webpage. Status code: {response.status_code}")

            yield html_content, page_no

    def scrape_sku(self):
        html_content_generator = self.__fetch_html_content__(self.offset, self.limit)
        sku_list = []

        for html_content, page_no in html_content_generator:
            soup = BeautifulSoup(html_content, 'html.parser')

            ul_class = 'products columns-4'
            div_class = 'mf-product-thumbnail'

            ul = soup.find('ul', class_='products columns-4')

            if not ul:
                logger.info(f"No unordered list found with class: {ul_class}")

            for li in ul.find_all('li'):
                # Extract the price, description, and link
                price = li.find('bdi').get_text(strip=True) if li.find('bdi') else 'N/A'
                price = price.lstrip("\u20b9")

                description = li.find(class_='woo-loop-product__title').get_text(strip=True) if li.find(
                    class_='woo-loop-product__title'
                ) else 'N/A'

                link = li.find(class_=div_class).find('img')['data-lazy-src'] if li.find(class_=div_class) else 'N/A'

                value = cache.get(description)
                if value and value['price'] == price:
                    logger.info(f"Skipping the update of {description}; data not stale!")
                    continue
                else:
                    sku_obj = SKU(price, description, link, page_no)
                    cache.set_with_timeout(description, vars(sku_obj), 10000)
                    sku_list.append(sku_obj)

        db = DatabaseFactory.create_database(DATABASE_TYPE)

        db.connect()
        SKU.bulk_update(db, sku_list)
        db.disconnect()

