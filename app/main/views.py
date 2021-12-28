#coding=utf-8
from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, current_app, abort
from werkzeug.exceptions import InternalServerError
from . import main
from .. import db
from .forms import NameForm 

app = current_app

@main.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
      		
			session['known'] = True 
			abort(404)

   
		session['name'] = form.name.data
	# 	return redirect(url_for('.index'))

	# app.logger.debug('this is a DEBUG message')
	# app.logger.info('this is a INFO message')
	# app.logger.warning('this is a WARNING message')
	# app.logger.error('this is a ERROR message')
	# app.logger.critical('this is a CRITICAL message')

	return render_template('index.html', 
					form=form, 
					name=session.get('name'), 
					known=session.get('known', False), 
					current_time=datetime.utcnow())