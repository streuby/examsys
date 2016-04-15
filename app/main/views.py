#coding=utf-8
from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .. import db
from .forms import NameForm 

@main.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash(u'看来你修改了名字！')
			session['known'] = False
		
		session['known'] = True 
		session['name'] = form.name.data
		return redirect(url_for('.index'))

	return render_template('index.html', 
					form=form, 
					name=session.get('name'), 
					known=session.get('known', False), 
					current_time=datetime.utcnow())

