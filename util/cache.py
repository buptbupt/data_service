from flask_cache import Cache
from conf import CACHE_CONFIG
cache = Cache(config=CACHE_CONFIG)
