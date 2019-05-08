# -*- coding: utf-8 -*-
import json
from flask import request, Blueprint


price = Blueprint("price", __name__)

@price.route("/input_price")
def input_price(socket):
     while not socket.closed:
        data = socket.receive()
        socket.send(json.dumps({'code': 0, 'msg': 'success', 'data':{}}))


