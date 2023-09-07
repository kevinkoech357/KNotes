#!/usr/bin/env python3

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# define a database and initiliaze
db = SQLAlchemy()
# give db a name
DB_NAME = "database.db"


def create_app():
    
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config["SECRET_KEY"] = "notasecret iguess"
    # configure database location, will be in app directory
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initiliaze database
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/") 
    app.register_blueprint(auth, url_prefix="/") 

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # looks for primary key

    return app

def create_database(app):

    with app.app_context():
        db.create_all()
        print('Database created successfully')
