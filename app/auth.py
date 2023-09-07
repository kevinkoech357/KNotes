#!/usr/bin/env python3

# Blueprint means it has all urls defined
# render_template returns specified html
# request shows all info sent by form
# flash is used to flash messages onscreen

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in succesfully!.', category='success')
                login_user(user, remember=True)

                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password. Try again!', category='error')
        else:
            flash('Email doesn\t exist!.', category='error')

    return render_template('login.html', user=current_user)

@auth.route("/logout")
@login_required
def logout():

    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstname')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(email=email).first

        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 3:
            flash('First Name must be greater than 2 characters.', category='error')
        elif password != confirm_password:
            flash('Passwords don\'t match.', category='error')
        elif len(password) < 8:
            flash('Password must be greater than 7 characters.', category='error')
        else:
            # take user input i.e email, first name and password
            # hash the password
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user) # add user to db
            db.session.commit() # update db
            login_user(user, remember=True) # log-ins user after acc creation

            flash('Account created succesfully.', category='success')

            return redirect(url_for('views.home')) # redirect to homepage

    return render_template('sign_up.html', user=current_user)
