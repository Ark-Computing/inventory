from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from .db.database import db
import os

def create_app():
    bcrypt = Bcrypt()
    app = Flask(__name__, template_folder=os.path.abspath('./templates'))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db.init_app(app)

    from arkinventory.client.routes import client_bp
    app.register_blueprint(client_bp, url_prefix='')

    

    with app.app_context():
        db.create_all()

    return app
