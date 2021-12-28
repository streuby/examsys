#coding=utf-8
from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import login_user, logout_user, login_required

from app.errors.handlers import InvalidUsage
from . import auth
from app.models import User, db
from .forms import LoginForm, ChangePasswordForm, RegisterForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	try:	
		
		if form.validate_on_submit():
			user = User.query.filter_by(username=form.username.data).first() or None

			# if user is not None and user.verify_password(form.password.data):
			# 	login_user(user, form.remember_me.data)
			# 	return redirect(request.args.get('next') or url_for('main.index', known = True))

			flash(u'Invalid username or password')
	except Exception as e:
		raise InvalidUsage('AN ERROR OCCURED', e, '', e.status_code)
	return render_template('auth/login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	
	if form.validate_on_submit():
		user = User(email=form.email.data,
			username=form.username.data,
			firstname=form.firstname.data,
			middlename=form.middlename.data,
			lastname=form.lastname.data,
			password=form.password.data) or None

        # add employee to the database
		if user is not None:
			db.session.add(user)
			db.session.commit()
			login_user(user)
			flash(u'You have successfully registered! You may now login.')
			return redirect(request.args.get('next') or url_for('main.index', known=True))
	return render_template('auth/register.html', form=form)


@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash(u'You have logged out of the system.')
	return redirect(url_for('main.index'))


@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
	form = ChangePasswordForm()


	return render_template('auth/change_password.html', form=form)
