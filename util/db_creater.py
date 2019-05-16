import random
from app import app
from util.db import db
from product.models import Product, ProductClass
from product.ops import create_product_without_save, create_product_class

db.drop_all(app=app)
db.create_all(app=app)

app.app_context().push()
db.init_app(app)
product_class_id_list = [None]


def init_product_class(num):
    root_class = create_product_class(dict(
        product_class_name={'chinese': '全部', 'english': 'all'},
        product_class_level=1
    ))
    product_class_id_list.append(root_class.id)
    for i in range(num):
        node_class = create_product_class(dict(
            product_class_name={
                'chinese': '1级{:0>2d}'.format(i),
                'english': 'level1_{:0>2d}'.format(i)
            },
            product_class_level=2,
            product_class_parent_id=root_class.id
        ))
        product_class_id_list.append(node_class.id)


init_product_class(5)


def init_product(num):
    for i in range(num):
        create_product_without_save(dict(
            product_name={
                'chinese': '测试产品{:0>2d}'.format(i),
                'english': 'test_product_{:0>2d}'.format(i)
            },
            product_code='P{:0>6d}'.format(i),
            product_status="测试状态",
            product_price=[['03:00', 4.2], ['12:00', 3.9], ['20:30', 7.1]],
            product_class_id=random.choice(product_class_id_list)
        ))
    db.session.commit()


init_product(20)
