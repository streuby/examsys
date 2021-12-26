#coding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField(u'Please enter your name：', validators=[DataRequired()])
    submit = SubmitField(u'Submit')
