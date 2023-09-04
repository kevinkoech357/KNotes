#!/usr/bin/env python3

# Blueprint means it has all urls defined
# render_template returns specified html
# request shows all info sent by form
# flash is used to flash messages onscreen

from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    # request allows us to get information that was sent into the form
    data = request.form
    # prints data => example: ImmutableMultiDict([('email', 'kev@gmail.com'), ('password', '1234')])
    print(data)
    return render_template('login.html')

@auth.route("/logout")
def logout():

    return render_template('home.html')

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password = request.form.get('form')
        confirm_password = request.form.get('confirm_password')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstname) < 3:
            flash('First Name must be greater than 2 characters.', category='error')
        elif password != confirm_password:
            flash('Passwords don\'t match.', category='error')
        elif len(password) < 8:
            flash('Password must be greater than 7 characters.', category='error')
        else:
            # add user to database
            flash('Account created succesfully.', category='success')
    return render_template('sign_up.html')
