from flask import Flask
from celery import Celery
from conf import CELERY_CONFIG
from util.db import db
from conf import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

celery = Celery(__name__, broker=CELERY_CONFIG['CELERY_BROKER_URL'])
celery.conf.update(**CELERY_CONFIG)

