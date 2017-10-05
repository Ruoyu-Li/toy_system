from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User

@app.route('/', methods = ['GET', 'POST'])
@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
		login_name = form.username.data
		u = User.query.filter_by(username = login_name).all()
		if len(u):
			return redirect('/index/%s' %login_name)
		else:
			return redirect('/login')
	return render_template('login.html',
		title = 'Sign in',
		form = form)

@app.route('/index/<username>')
def index(username):
	return render_template('index.html',
		username = username)