import uuid
from product.models import Product, ProductClass
from util.db import db
from util.cache import cache
from util.check import check_create_obj_dict
from util.search import get_search_list


@cache.memoize(timeout=10)
def get_product_tree(limit=10):
    root = ProductClass.query.filter_by(product_class_level=1).one()
    return recursive_product_class_node(root, limit)


def recursive_product_class_node(node, limit):
    res = {'product_list': []}
    for product in node.product_list.order_by(
            Product.product_code).all()[:limit]:
        res['product_list'].append(product.brief())
    if node.children:
        res['children'] = []
        for child in node.children:
            res['children'].append(recursive_product_class_node(child, limit))
    return res


def get_product_info(args):
    product_obj = None
    if 'id' in args:
        product_obj = Product.query.get(args.get('id', ''))
    if 'product_code' in args:
        product_obj = Product.query.filter_by(
            product_code=args.get('product_code', '')).first()
    if not product_obj:
        raise '未找到产品'
    return product_obj.to_dict()


def create_product(product_dict):
    _check_create_product(product_dict)
    return _create_product_obj(product_dict)


def create_product_without_save(product_dict):
    _check_create_product(product_dict)
    return _create_product_obj(product_dict, save=False)


def create_product_class(product_class_dict):
    _check_create_product_class(product_class_dict)
    return _create_product_class_obj(product_class_dict)


def list_product(args):
    res = []
    offset = int(args.pop('offset', 0))
    limit = int(args.pop('limit', 10))
    query = Product.query
    if 'key_words' in args:
        query = query.filter(Product.search_list.any(
            args.pop('key_words', '')))
    query = query.order_by(Product.product_code)
    for item in query.all()[offset:offset+limit]:
        res.append(item.to_dict())
    return res


def _check_create_product(product_dict):
    check_create_obj_dict(product_dict)


def _create_product_obj(product_dict, save=True):
    product_dict['id'] = uuid.uuid1().hex
    product_obj = Product(**product_dict)
    product_obj.search_list = get_search_list(
        cut_list=list((product_obj.product_name or {}).values()),
        not_cut_list=[product_obj.product_code])
    db.session.add(product_obj)
    if save:
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
