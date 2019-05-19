from celery import Celery
from conf import CELERY_CONFIG

celery = Celery()
celery.conf.update(CELERY_CONFIG)
