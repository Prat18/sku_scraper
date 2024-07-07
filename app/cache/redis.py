import json

import redis
from app.core.config import settings

CACHE_CONFIG = settings.CACHE_CONFIG


class RedisCache:
    def __init__(self):
        self.redis_client = redis.StrictRedis(
            host=CACHE_CONFIG['host'],
            port=CACHE_CONFIG['port'],
            password=CACHE_CONFIG['password']
        )

    def set_with_timeout(self, key, value, timeout_seconds):
        self.redis_client.set(key, json.dumps(value), ex=timeout_seconds)

    def get(self, key):
        cached_value = self.redis_client.get(key)
        if cached_value:
            return json.loads(cached_value.decode('utf-8'))  # Decode bytes to string if necessary
        return None

    def check_after_timeout(self, key):
        cached_value_after_timeout = self.redis_client.get(key)
        if cached_value_after_timeout:
            return cached_value_after_timeout.decode('utf-8')  # Decode bytes to string if necessary
        return None
