from app import app
from util.db import db

db.create_all(app=app)