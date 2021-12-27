from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import logging

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
    
    if __name__ != '__main__':
        gunicorn_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)

    return app
