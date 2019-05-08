from flask_cache import Cache    
cache = Cache(config={
    "CACHE_TYPE": "redis",
    "CACHE_REDIS_HOST": "127.0.0.1",
    "CACHE_REDIS_PORT": 6379,
    "CACHE_REDIS_DB": 0,
    "CACHE_REDIS_PASSWORD": "",
})
