import uuid
from product.models import Product, ProductClass
from util.db import db
from util.check import check_create_obj_dict


def create_product(product_dict):
    _check_create_product(product_dict)
    return _create_product_obj(product_dict)


def create_product_class(product_class_dict):
    _check_create_product_class(product_class_dict)
    return _create_product_class_obj(product_class_dict)


def list_product(args):
    res = []
    for item in Product.query.limit(args.pop('num', 10)):
        res.append(item.to_dict())
    return res


def _check_create_product(product_dict):
    check_create_obj_dict(product_dict)


def _create_product_obj(product_dict):
    product_dict['id'] = uuid.uuid1().hex
    product_obj = Product(**product_dict)
    db.session.add(product_obj)
    db.session.commit()
    return product_obj


def _check_create_product_class(product_class_dict):
    check_create_obj_dict(product_class_dict)


def _create_product_class_obj(product_class_dict):
    product_class_dict['id'] = uuid.uuid1().hex
    product_class_obj = ProductClass(**product_class_dict)
    db.session.add(product_class_obj)
    db.session.commit()
    return product_class_obj
