from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from arkinventory.models import *

app = Flask(__name__)
db = SQLAlchemy()
db.init_app(app)

with app.app_context():
    db.create_all()
