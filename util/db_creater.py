from app import app
from util.db import db
from product.models import Product

db.create_all(app=app)