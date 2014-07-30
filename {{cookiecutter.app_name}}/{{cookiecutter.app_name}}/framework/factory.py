# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.app_name }}.framework.factory
    {{ "~" * (cookiecutter.app_name ~ ".framework.factory")|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
import os

from celery import Celery
from flask import Flask
from flask.ext.security import SQLAlchemyUserDatastore
from passlib.context import CryptContext
from raven.contrib.flask import Sentry

from . import security
from .extensions import (
    db,
    jwt,
    migrate,
)
from .middleware import HTTPMethodOverrideMiddleware
from ..models.users import User, Role


def create_app(package_name, package_path,
               settings_override=None):
    """
    Returns a :class:`Flask` application instance configured with common
    functionality for the webapp.

    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
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

    # Password Context
    app.extensions['pwd_context'] = CryptContext(schemes=["bcrypt"])

    # User Datastore
    app.extensions['user_datastore'] = SQLAlchemyUserDatastore(db, User, Role)

    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    # Flask-JWT
    jwt.init_app(app)
    jwt.authentication_handler(security.authenticate)
    jwt.user_handler(security.load_user)

    # Sentry - only for production 
    if not app.debug and not app.testing and 'SENTRY_DSN' in app.config:
        sentry = Sentry(app)

    # Middleware
    app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

    return app


def create_celery_app(app=None):
    app = app or create_app('{{ cookiecutter.app_name }}',
                            os.path.dirname(__file__))
    # celery must be configured with the proper broker
    # when it is initialized; this 
    broker = app.config.get('CELERY_BROKER_URL', None)
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
