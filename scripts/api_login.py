from flask import Flask, redirect, url_for, render_template, request, session
from flask import Blueprint, abort
import json
import forms
import helpers

auth = Blueprint('auth', __name__,
                        template_folder='templates')

@auth.route('/', methods=['GET', 'POST'])
def login():
    if not session.get('logged_in'):
        form = forms.LoginForm(request.form)
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = request.form['password']
            print(username)
            print(password)
            if form.validate():
                if helpers.credentials_valid(username, password):
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'Login successful'})
                return json.dumps({'status': 'Invalid user/pass'})
            return json.dumps({'status': 'Both fields required'})
        return render_template('login.html', form=form)
    user = helpers.get_user()
    return render_template('home.html', user=user)


@auth.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('auth.login'))
