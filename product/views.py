# -*- coding: utf-8 -*-
import json
from flask import request, Blueprint
from product import ops
from product.models import Product
from util.api import APIResult, api_wrap

product = Blueprint("product", __name__)


@product.route("/list_product", methods=["GET"])
@api_wrap
def list_product():
    res = ops.list_product(request.args.to_dict() or {})
    return APIResult(0, res)


@product.route("/add_product", methods=["POST"])
@api_wrap
def add_product():
    ops.create_product(request.json or {})
    return APIResult(0)


@product.route("/get_product", methods=["GET"])
@api_wrap
def get_product():
    item = Product.query.get(request.args.to_dict().get('id', ''))
    return APIResult(0, item.to_dict()) if item else APIResult(1, '无法找到')