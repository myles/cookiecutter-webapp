# -*- coding: utf-8 -*-
"""
    framwork.factory
    ~~~~~~~~~~~~~~~~

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
import os

from celery import Celery
from flask import Flask
from flask.ext.security import SQLAlchemyUserDatastore
#from flask.ext.social import SQLAlchemyConnectionDatastore
from raven.contrib.flask import Sentry

from . import helpers
from .extensions import (
    db,
    jwt,
    mail,
    migrate,
    security,
)
from .middleware import HTTPMethodOverrideMiddleware
from ..forms.security import ExtendedRegisterForm
from ..models.users import User, Role, Connection

def create_app(package_name, package_path,
               settings_override=None,
               register_blueprints=True,
               register_security_blueprint=True):
    """
    Returns a :class:`Flask` application instance configured with common
    functionality for the webapp.

    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    :param register_blueprints: flag to specify if the factory should auto-discover
                                blueprints to be register to the application.
                                Defaults to `True`.
    :param register_security_blueprint: flag to specify if the Flask-Security
                                        Blueprint should be registered. Defaults
                                        to `True`.
    """
    # Instance Path
    instance_path = os.environ.get("{{ cookiecutter.app_name | upper }}_INSTANCE_PATH", None)

    # Create App
    if instance_path:
        app = Flask(package_name, instance_path=instance_path)
    else:
        app = Flask(package_name, instance_relative_config=True)

    # Initialize settings
    app.config.from_object("{{ cookiecutter.app_name }}.settings")
    app.config.from_pyfile("settings.cfg", silent=True)
    app.config.from_object(settings_override)

    # Base Extensions
    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    security.init_app(app, SQLAlchemyUserDatastore(db, User, Role),
                      register_blueprint=register_security_blueprint,
                      register_form=ExtendedRegisterForm)

    # Sentry - only for production 
    if not app.debug and not app.testing and 'SENTRY_DSN' in app.config:
        sentry = Sentry(app)

    # Blueprints
    if register_blueprints:
        helpers.register_blueprints(app, package_name, package_path)

    # Middleware
    app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

    return app


def create_celery_app(app=None):
    app = app or create_app('{{ cookiecutter.app_name }}', os.path.dirname(__file__))
    broker = app.config.get('CELERY_BROKER_URL', None) # 'redis://127.0.0.1:6379'
    celery = Celery(__name__, broker=broker)
    celery.config_from_object(app.config, force=True)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery
