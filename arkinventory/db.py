from arkinventory import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app.config["SQLSLCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db.init_app(app)


class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12),  unique=True,  nullable=False)
    email    = db.Column(db.String(120),  unique=True,  nullable=False)
    password = db.Column(db.String(60),  unique=False, nullable=False)


class PartTemplate(db.Model):
    id           = db.Column(db.Integer,  primary_key=True)
    name         = db.Column(db.String,   unique=False, nullable=False)
    price        = db.Column(db.Float,    unique=False, nullable=False)
    dop          = db.Column(db.Datetime, unique=False, nullable=False)
    # TODO: Determine most intuitive backref names
    manufacturer = db.relationship('Manufacturer', backref='man_name', lazy=True, nullable=False)
    build        = db.relationship('Build', backref='build_name', lazy=True, nullable=True)


class Manufacturer(db.Model):
    id           = db.Column(db.Integer,  primary_key=True)
    name         = db.Column(db.String,   unique=False, nullable=False)
    partner      = db.Column(db.Boolean, nullable=False, default=False)
    sponsor      = db.Column(db.Boolean, nullable=False, default=False)


class Build(db.Model):
    id           = db.Column(db.Integer,  primary_key=True)
    name         = db.Column(db.String,   unique=False, nullable=False)
    # TODO: One-to-many relationship between Build and all Parts

