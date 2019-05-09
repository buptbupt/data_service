# -*- coding: utf-8 -*-
import logging
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_sockets import Sockets
from flask_compress import Compress
from util.cache import cache
from price.views import price
from conf import *

logging.basicConfig(level=logging.INFO, filename='app.log')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
sockets = Sockets(app)
cache.init_app(app)
Compress(app)
db = SQLAlchemy(app)

sockets.register_blueprint(price, url_prefix="/price")


if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 80), app, handler_class=WebSocketHandler)
    server.serve_forever()
