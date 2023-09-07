#!/usr/bin/env python3

# remember db is in same directory
# flask_login module has UserMixin class
# func.now lets us get current date and time

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    """
    Define note class
    """

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    """
    Define class user
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    notes = db.relationship('Note')
