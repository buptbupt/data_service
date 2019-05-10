# -*- coding: utf-8 -*-
import json
from flask import request, Blueprint
from price import ops
from price.models import Price
from util.api import APIResult

price = Blueprint("price", __name__)
price_ws = Blueprint("price_ws", __name__)

@price_ws.route("/input_price")
def input_price(socket):
    while not socket.closed:
        data = socket.receive()
        socket.send(json.dumps({'code': 0, 'msg': 'success', 'data':{}}))


@price.route("/add_price", methods=["GET"])
def get_price():
    
    return APIResult(0)


@price.route("/get_price", methods=["GET"])
def get_price():
    item = Price.query.get(id=request.args.to_dict().get('id'))
    if item:
        return APIResult(0, item.to_dict())
    else:
        return APIResult(1, msg='无此价格')