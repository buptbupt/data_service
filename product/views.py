# -*- coding: utf-8 -*-
import json
from flask import request, Blueprint
from product import ops
from product.models import Product
from util.api import APIResult, api_wrap

product = Blueprint("product", __name__)



@product.route("/add_product", methods=["GET"])
@api_wrap
def add_product():
    try:
        ops.create_product(request.json or {})
    except:
        import traceback
        return APIResult(1, msg=traceback.format_exc())
    return APIResult(0)


@product.route("/get_product", methods=["GET"])
@api_wrap
def get_product():
    item = Product.query.get(request.args.to_dict().get('id', ''))
    if item:
        return APIResult(0, item.__dict__)
    else:
        return APIResult(1, msg='无此价格')