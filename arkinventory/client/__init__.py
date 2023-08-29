from db import models
from .. import app
from flask_sqlalchemy import SQLAlchemy, create_all

app.config['SQLALCHEMY_DATABASE_URI'] = '' # TODO: Generate database URI

db = SQLAlchemy()

db.create_all()


