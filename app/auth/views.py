#coding=utf-8
from flask import render_template, flash, redirect, url_for, request
from flask.ext.login import login_user, logout_user, login_required
from . import auth
from ..models import User 
from .forms import LoginForm, ChangePasswordForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()

		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('main.index'))

		flash(u'无效用户名或密码。')
	return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash(u'你已经退出系统。')
	return redirect(url_for('main.index'))


@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
	form = ChangePasswordForm()


	return render_template('auth/change_password.html', form=form)
