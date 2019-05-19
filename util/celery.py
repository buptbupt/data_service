from flask import Flask
from celery import Celery
from conf import CELERY_CONFIG

celery = Celery()
celery.conf.update(**CELERY_CONFIG)


def create_app():
    app = Flask(__name__)
    celery.conf.update(**CELERY_CONFIG)
    return app
