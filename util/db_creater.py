from app import app
from util.db import db
from product.models import Product

db.drop_all(app=app)
db.create_all(app=app)