#coding=utf-8
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, EqualTo


class LoginForm(Form):
	username = StringField(u'用户名', validators=[Required()])
	password = PasswordField(u'密码', validators=[Required()])
	remember_me = BooleanField(u'记住我')
	submit = SubmitField(u'登录')


class ChangePasswordForm(Form):
	old_password = PasswordField(u'原始密码', validators=[Required()])
	password = PasswordField(u'新密码', validators=[
		Required(), EqualTo('password2', message=u'两次输入的密码必须一致')])
	password2 = PasswordField(u'请确认密码', validators=[Required()])
	submit = SubmitField(u'修改密码')

