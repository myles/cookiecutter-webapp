# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.app_name }}.framework.factory
    {{ "~" * (cookiecutter.app_name ~ ".framework.factory")|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
import logging
import os

from flask import Flask
from flask.ext.security import SQLAlchemyUserDatastore
from raven.contrib.flask import Sentry

from .extensions import *
from .middleware import HTTPMethodOverrideMiddleware
from .security import authenticate, load_user, make_payload
from ..models.users import User, Role

_log = logging.getLogger(__name__)

__all__ = ('create_app',)

def create_app(package_name, package_path, settings_override=None,
               security_register_blueprint=False):
    """
    Returns a :class:`Flask` application instance configured with common
    functionality for the webapp.

    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    :param security_register_blueprint: register views for flask-security
    """
    # Instance Path
    instance_path = os.environ.get("{{ cookiecutter.app_name | upper }}_INSTANCE_PATH", None)

    # Create App
    if instance_path:
        app = Flask(package_name, instance_path=instance_path)
        _log.info("Flask initialized with instance path: %s", instance_path)
    else:
        app = Flask(package_name, instance_relative_config=True)
        _log.info("Flask initialized using a relative instance path")

    # Initialize settings
    app.config.from_object("{{ cookiecutter.app_name }}.settings")
    app.config.from_pyfile("settings.cfg", silent=True)
    app.config.from_object(settings_override)

    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    # Flask-Mail
    mail.init_app(app)

    # Flask-Security
    security.init_app(app, SQLAlchemyUserDatastore(db, User, Role),
                      register_blueprint=security_register_blueprint)

    # Flask-JWT
    jwt.init_app(app)
    jwt.authentication_handler(authenticate)
    jwt.payload_handler(make_payload)
    jwt.user_handler(load_user)

    # Sentry - only for production 
    if not app.debug and not app.testing and 'SENTRY_DSN' in app.config:
        sentry = Sentry(app)

    # Middleware
    app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

    _log.info("Flask framework app created.")
    return app
