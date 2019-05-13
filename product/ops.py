from product.models import Product
from util.db import db

def create_product(product_dict):
    if 'id' in product_dict:
        raise '不可包含id字段'
    db.session.add(Product(**product_dict))
    db.session.commit()