from flask import Flask
from celery import Celery
from conf import CELERY_CONFIG
from app import app

app.app_context().push()

celery = Celery(__name__, broker=CELERY_CONFIG['CELERY_BROKER_URL'])
celery.conf.update(**CELERY_CONFIG)

