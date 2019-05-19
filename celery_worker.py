from app import create_app
from util.celery import celery

app = create_app()
app.app_context().push()
