from util.db import db


class Price(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    source = db.Column(db.String(32))
    product_code = db.Column(db.String(32))
    product_abbr_name = db.Column(db.String(128))
    today_opening_price = db.Column(db.DECIMAL())
    yesterday_closing_price = db.Column(db.DECIMAL())
    current_price = db.Column(db.DECIMAL())
    highest_price = db.Column(db.DECIMAL())
    lowest_price = db.Column(db.DECIMAL())
    buying_price = db.Column(db.DECIMAL())
    selling_price = db.Column(db.DECIMAL())
    dealed_number = db.Column(db.Integer)
    dealed_amount = db.Column(db.DECIMAL())
    buying_number_1 = db.Column(db.Integer)
    buying_price_1 = db.Column(db.DECIMAL())
    buying_number_2 = db.Column(db.Integer)
    buying_price_2 = db.Column(db.DECIMAL())
    buying_number_3 = db.Column(db.Integer)
    buying_price_3 = db.Column(db.DECIMAL())
    buying_number_4 = db.Column(db.Integer)
    buying_price_4 = db.Column(db.DECIMAL())
    buying_number_5 = db.Column(db.Integer)
    buying_price_5 = db.Column(db.DECIMAL())
    selling_number_1 = db.Column(db.Integer)
    selling_price_1 = db.Column(db.DECIMAL())
    selling_number_2 = db.Column(db.Integer)
    selling_price_2 = db.Column(db.DECIMAL())
    selling_number_3 = db.Column(db.Integer)
    selling_price_3 = db.Column(db.DECIMAL())
    selling_number_4 = db.Column(db.Integer)
    selling_price_4 = db.Column(db.DECIMAL())
    selling_number_5 = db.Column(db.Integer)
    selling_price_5 = db.Column(db.DECIMAL())
    price_date = db.Column(db.DATE())
    price_time = db.Column(db.TIME())

    create_time = db.Column(db.DATETIME())

    def __repr__(self):
        return '<Price %r>' % self.id

    def to_dict(self):
        return dict(

        )