#coding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email


class LoginForm(FlaskForm):
	username = StringField(u'Username', validators=[DataRequired()])
	password = PasswordField(u'Password', validators=[DataRequired()])
	remember_me = BooleanField(u'Remeber me')
	submit = SubmitField('Login', render_kw={"class":"btn btn-primary btn-sm submit", 
                                        "type":"submit", "data-required":"login-required"})
 
class RegisterForm(FlaskForm):
	username = StringField(u'Username', validators=[DataRequired()])
	firstname = StringField(u'Firstname', validators=[DataRequired()])
	middlename = StringField(u'Middlename')
	lastname = StringField(u'Surname', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField(u'Create Password', validators=[
		DataRequired(), EqualTo('password2', message=u'Password must be the same')])
	password2 = PasswordField(u'Repeat Password', validators=[DataRequired()])
	submit = SubmitField('Register', render_kw={"class":"btn btn-primary btn-sm submit", 
                                        "type":"submit", "data-required":"login-required"})


class ChangePasswordForm(FlaskForm):
	old_password = PasswordField(u'Old password', validators=[DataRequired()])
	password = PasswordField(u'New Password', validators=[
		DataRequired(), EqualTo('password2', message=u'Password must be the same')])
	password2 = PasswordField(u'Repeat New Password', validators=[DataRequired()])
	submit = SubmitField(u'Submit')

