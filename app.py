# -*- coding: utf-8 -*-
import conf
import logging
from flask import Flask, request
from flask_sockets import Sockets
from flask_compress import Compress
from util.cache import cache
from price.views import price_blueprint

logging.basicConfig(level=logging.INFO, filename='app.log')

app = Flask(__name__)
sockets = Sockets(app)
cache.init_app(app)
Compress(app)

app.register_blueprint(price_blueprint, url_prefix="/price")




if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 80), app, handler_class=WebSocketHandler)
    server.serve_forever()
