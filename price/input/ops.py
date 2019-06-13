import uuid
from price.models import Price


def create_price_obj(price_dict, db, save=True):
    price_dict['id'] = uuid.uuid1().hex
    price_obj = Price(**price_dict)
    db.session.add(price_obj)
    if save:
        db.session.commit()
    return price_obj