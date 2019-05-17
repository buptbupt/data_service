# -*- coding: utf-8 -*-
import json
from flask import request, Blueprint
from price import ops
from price.models import Price
from util.api import APIResult, api_wrap

price = Blueprint("price", __name__)
price_ws = Blueprint("price_ws", __name__)

@price_ws.route("/input_price")
def input_price(socket):
    while not socket.closed:
        data = socket.receive()
        ops.price_data_mapper(data)
        socket.send(json.dumps({'code': 0, 'msg': 'success', 'data':{}}))

