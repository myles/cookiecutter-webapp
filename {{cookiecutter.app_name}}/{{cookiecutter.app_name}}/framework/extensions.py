# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.app_name }}.framework.extensions
    {{ "~" * (cookiecutter.app_name ~ ".framework.extensions")|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.migrate import Migrate
migrate = Migrate()

from flask.ext.jwt import JWT
jwt = JWT()
