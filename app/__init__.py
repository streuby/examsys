import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler

from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    from app.errors import errors
    app.register_blueprint(errors)
    
    # @app.errorhandler(500)
    # def server_error(e):
    #     return """
    #     An internal error occurred: <pre>{}</pre>
    #     See logs for full stacktrace.
    #     """.format(e), 500
    
    # if config_name == 'production':
    #     gunicorn_error_logger = logging.getLogger('gunicorn.error')
    #     app.logger.handlers.extend(gunicorn_error_logger.handlers)
    #     app.logger.setLevel(logging.DEBUG)
    #     app.logger.debug('this will show in the log')
    
    # if __name__ != '__main__':
    #     gunicorn_logger = logging.getLogger('gunicorn.error')
    #     app.logger.handlers = gunicorn_logger.handlers
    #     app.logger.setLevel(gunicorn_logger.level)
    
    # Configure customer logger
    if not app.debug and not app.testing:
        # if app.config['MAIL_SERVER']:
        #     auth = None
        #     if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
        #         auth = (app.config['MAIL_USERNAME'],
        #                 app.config['MAIL_PASSWORD'])
        #     secure = None
        #     if app.config['MAIL_USE_TLS']:
        #         secure = ()
        #     mail_handler = SMTPHandler(
        #         mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
        #         fromaddr='no-reply@' + app.config['MAIL_SERVER'],
        #         toaddrs=app.config['ADMINS'], subject='Fliptz Failure',
        #         credentials=auth, secure=secure)
        #     mail_handler.setLevel(logging.ERROR)
        #     app.logger.addHandler(mail_handler)

        if not os.path.exists('/home/ubuntu/examsys/logs'):
            os.mkdir('/home/ubuntu/examsys/logs')
        file_handler = RotatingFileHandler('/home/ubuntu/examsys/logs/examsys.log',
                                           maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('examsys startup')

    return app
