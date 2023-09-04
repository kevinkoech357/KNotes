#!/usr/bin/env python3

# Blueprint means it has all urls defined
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    # render_template returns the specified html
    return render_template('home.html')


