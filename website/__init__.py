#!/usr/bin/env python3

from flask import Flask

def create_app():
    
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "notasecret iguess"

    return app
