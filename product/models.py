import datetime
from util.db import db


class Product(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    product_name = db.Column(db.JSON)
    product_code = db.Column(db.String(32), index=True, unique=True)
    product_price = db.Column(db.JSON)
    product_status = db.Column(db.String(32))
    product_class_id = db.Column(db.String(32), 
                                 db.ForeignKey('product_class.id'))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    lut = db.Column(db.DateTime, default=datetime.datetime.utcnow,
                    onupdate=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Product %r>' % self.product_name

    def to_dict(self):
        return dict(
            id=self.id,
            product_name=self.product_name,
            product_code=self.product_code,
            product_price=self.product_price,
            product_status=self.product_status,
            product_class=self.product_class and
            self.product_class.product_class_name
        )


class ProductClass(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    product_class_name = db.Column(db.JSON)
    product_class_level = db.Column(db.Integer)
    product_list = db.relationship(
        'Product', backref='product_class', lazy='dynamic')
    product_class_parent_id = db.Column(
        db.String(32), db.ForeignKey('product_class.id'))
    children = db.relationship(
        "ProductClass", backref=db.backref('parent', remote_side=[id]))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<ProductClass %r>' % self.product_class_name
