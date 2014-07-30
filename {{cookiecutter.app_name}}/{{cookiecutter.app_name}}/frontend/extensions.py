# -*- coding: utf-8 -*-
"""
    extensions.py
    ~~~~~~~~~~~~~

    Initialize Frontend Flask and Jinja extensions.

    :authro: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from ..framework.extensions import *

from flask.ext.debugtoolbar import DebugToolbarExtension
debug_toolbar = DebugToolbarExtension()

from flask.ext.mail import Mail
mail = Mail()

from flask.ext.security import Security
security = Security()
