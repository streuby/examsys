#coding=utf-8
import os
from pathlib import Path
home = str(Path.home())
basedir = os.path.abspath(os.path.dirname(__file__))
_basedir = str(basedir)


class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
   	#FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
	EXAM_ADMIN = os.environ.get('EXAM_ADMIN')
	EXAM_TITLE = os.environ.get('EXAM_TITLE') or u'Exam system' 
	
	@staticmethod
	def init_app(app):
		pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = os.environ.get("SECRET_KEY")
    FLASK_CONFIG='development'
    FLASK_APP= 'manage.py'
    DATABASE_URL='mysql+pymysql://root:PUBLICman09@localhost/examsys_db'
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:PUBLICman09@localhost/examsys_db'
    SECRET_KEY='p9Bv3Eid9$i01'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
