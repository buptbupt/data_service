from flask_cache import Cache
from conf import CACHE_REDIS_HOST
cache = Cache(config={
    "CACHE_TYPE": "redis",
    "CACHE_REDIS_HOST": CACHE_REDIS_HOST,
    "CACHE_REDIS_PORT": 6379,
    "CACHE_REDIS_DB": 0,
    "CACHE_REDIS_PASSWORD": "",
})
