from arkinventory import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app.config["SQLSLCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db.init_app(app)
