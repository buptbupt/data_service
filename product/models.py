from util.db import db

class Product(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    product_name = db.Column(db.JSON)
    product_code = db.Column(db.String(32), index=True)
    product_price = db.Column(db.JSON)
    product_status = db.Column(db.String(32))
    product_class = db.Column(db.String(32), db.ForeignKey('product_class.id'))
    

    def __repr__(self):
        return '<Product %r>' % self.id


class ProductClass(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    product_class_name = db.Column(db.String(32))
    product_class_level = db.Integer()
    product_list = db.relationship('Product', backref='product', lazy='dynamic')

    product_class_parent_id = db.Column(db.String(32), db.ForeignKey('product_class.id'))
    children = db.relationship("ProductClass", backref=db.backref('parent', remote_side=[id]))

    def __repr__(self):
        return '<ProductClass %r>' % self.id