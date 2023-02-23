from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "This is my key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(DB_NAME)
    db.init_app(app)

    from .auth import auth
    from .views import views

    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(views, url_prefix="/")

    from .models import User, Note
    
    create_database(app)

    return app



def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('created Database')
