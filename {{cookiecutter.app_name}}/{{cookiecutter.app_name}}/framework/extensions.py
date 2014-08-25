# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.app_name }}.framework.extensions
    {{ "~" * (cookiecutter.app_name ~ ".framework.extensions")|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.

    templated from https://github.com/ryanolson/cookiecutter-webapp
"""
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.migrate import Migrate
migrate = Migrate()

from flask.ext.jwt import JWT
jwt = JWT()

from flask.ext.mail import Mail
mail = Mail()

from flask.ext.security import Security
security = Security()

__all__ = ("db", "migrate", "jwt", "mail", "security", )
