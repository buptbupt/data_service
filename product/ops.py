import uuid
from product.models import Product, ProductClass
from util.db import db


def create_product(product_dict):
    if 'id' in product_dict:
        raise '不可包含id字段'
    product_dict['id'] = uuid.uuid1().hex
    product_obj = Product(**product_dict)
    db.session.add(product_obj)
    db.session.commit()
    return product_obj


def create_product_class(product_class_dict):
    if 'id' in product_class_dict:
        raise '不可包含id字段'
    product_class_dict['id'] = uuid.uuid1().hex
    product_class_obj = ProductClass(**product_class_dict)
    db.session.add(product_class_obj)
    db.session.commit()
    return product_class_obj


def list_product(args):
    res = []
    for item in Product.query.limit(args.pop('num', 10)):
        res.append(item.to_dict())
    return res
