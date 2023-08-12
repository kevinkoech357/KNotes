#!/usr/bin/env python3

from flask import Flask
from flask_bootstrap import Bootstrap4

def create_app():
    
    app = Flask(__name__)
    bootstrap = Bootstrap4(app)
    app.config["SECRET_KEY"] = "notasecret iguess"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/") 
    app.register_blueprint(auth, url_prefix="/") 

    return app
