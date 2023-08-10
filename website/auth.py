#!/usr/bin/env python3

from flask import Blueprint # Blueprint means it has all urls defined

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():

    return "<p>Login</p>"

@auth.route("/logout")
def logout():

    return "<p>Logout</p>"

@auth.route("/sign-up")
def sign_up():

    return "<p>Sign Up</p>"
