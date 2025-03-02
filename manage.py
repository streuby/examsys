#!/usr/bin/env python
#coding=utf-8
import os
from os.path import join, dirname
from dotenv import load_dotenv
from app import create_app, db
from app.models import User, Role
# from flask_script import Manager, Shell
from flask_migrate import Migrate

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
#manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
    
# manager.add_command("shell", Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)


# @manager.command
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    # manager.run()
    app.run(host='127.0.0.1', port=5999)