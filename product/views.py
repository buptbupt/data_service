# -*- coding: utf-8 -*-
import json
from flask import request, Blueprint
from product import ops
from product.models import Product
from util.api import APIResult, api_wrap
from util.cache import cache

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


@cache.cached(5)
@product.route("/get_product", methods=["GET"])
@api_wrap
def get_product():
    res = ops.get_product_info(request.args.to_dict() or {})
    return APIResult(0, res)


@product.route("/get_product_tree", methods=["GET"])
@api_wrap
def get_product_tree():
    limit = int(request.args.to_dict().get('limit', 10))
    res = ops.get_product_tree(limit)
    return APIResult(0, res)


@product.route("/test_celery", methods=["GET"])
@api_wrap
def test_celery():
    ops.test_celery.delay((request.args.to_dict() or {}).get('test', ''))
    return APIResult(0, msg='已添加任务')
