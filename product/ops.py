import uuid
from product.models import Product, ProductClass
from util.db import db


def create_product(product_dict):
    if 'id' in product_dict:
        raise '不可包含id字段'
    product_dict['id'] = uuid.uuid1().hex
    db.session.add(Product(**product_dict))
    db.session.commit()


def create_product_class(product_class_dict):
    if 'id' in product_class_dict:
        raise '不可包含id字段'
    product_class_dict['id'] = uuid.uuid1().hex
    db.session.add(ProductClass(**product_class_dict))
    db.session.commit()


def list_product(args):
    res = []
    for item in Product.query.limit(args.pop('num', 10)):
        res.append(item.to_dict())
    return res
