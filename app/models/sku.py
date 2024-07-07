from logger.logger import Logger

logger = Logger('scraper').get_logger()


class SKU:
    def __init__(self, price, description, link, page_no):
        self.price = price
        self.description = description
        self.link = link
        self.page_no = page_no

    @staticmethod
    def bulk_update(db, sku_list):
        json_data = db.fetch_all()
        sku_list = [vars(sku) for sku in sku_list]
        target_dict = {item['description']: item for item in json_data}

        for sku in sku_list:
            if sku['description'] in target_dict:
                logger.info(f"updating sku: {sku['description']}, page_no: {sku['page_no']}")
                target_dict[sku['description']].update(sku)
            else:
                logger.info(f"appending sku: {sku['description']}, page_no: {sku['page_no']}")
                target_dict[sku['description']] = sku

        json_data[:] = target_dict.values()
