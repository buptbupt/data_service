
SQLALCHEMY_DATABASE_URI = 'postgresql://root:19950403@172.17.0.4/data'

CACHE_CONFIG = {
    "CACHE_TYPE": "redis",
    "CACHE_REDIS_HOST": '172.17.0.6',
    "CACHE_REDIS_PORT": 6379,
    "CACHE_REDIS_DB": 0,
    "CACHE_REDIS_PASSWORD": "",
}

# CACHE_CONFIG = {'CACHE_TYPE': 'simple'}
# SQLALCHEMY_DATABASE_URI = 'sqlite:///foo.db'
