DEBUG = False

if DEBUG:

    CACHE_CONFIG = {'CACHE_TYPE': 'simple'}

    SQLALCHEMY_DATABASE_URI = 'sqlite:///foo.db'

else:

    SQLALCHEMY_DATABASE_URI = 'postgresql://root:19950403@172.17.0.4/data'

    CACHE_CONFIG = {
        "CACHE_TYPE": "redis",
        "CACHE_REDIS_HOST": '172.17.0.2',
        "CACHE_REDIS_PORT": 6379,
        "CACHE_REDIS_DB": 0,
        "CACHE_REDIS_PASSWORD": "",
    }

    CELERY_CONFIG = dict(
        CELERY_BROKER_URL='redis://172.17.0.2:6379/1',
        CELERY_RESULT_BACKEND='redis://172.17.0.2:6379/1',
        CELERY_IMPORTS=['price.input.main']
    )
