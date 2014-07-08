# -*- coding: utf-8 -*-
"""
    frontend
    ~~~~~~~~

    :author: {{ cookiecutter.author }}
    :copyright: (c) {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from functools import wraps

from flask import render_template

from . import assets
from . import extensions
from . import views
from ..framework import factory

def create_app(settings_override=None):
    """Returns a {{ cookiecutter.app_name }} frontend application instance"""
    app = factory.create_app(__name__, __path__, settings_override)

    # Init assets
    assets.init_app(app)

    # Flask-DebugToolbar
    extensions.debug_toolbar.init_app(app)

    # Flask-Babel
    # extensions.babel.init_app(app)

    # Register custom error handlers
    #if not app.debug:
    #    for e in [500, 404]:
    #        app.errorhandler(e)(handle_error)

    # Initialize Views
    views.init_app(app)

    return app


def handle_error(e):
    return render_template('errors/%s.html' % e.code), e.code

