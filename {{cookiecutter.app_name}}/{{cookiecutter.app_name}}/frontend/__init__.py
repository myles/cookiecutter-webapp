# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.app_name }}.frontend.factory
    {{ "~" * (cookiecutter.app_name ~ ".frontend.factory")|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from . import assets
from . import extensions
from . import views

def create_app(settings_override=None):
    """Returns a {{ cookiecutter.app_name }} frontend application instance"""

    from flask import render_template
    from flask.ext.security import SQLAlchemyUserDatastore

    from .forms import security

    from .. import framework
    from ..framework.sql import db
    from ..models.users import User, Role, Connection

    app = framework.create_app(__name__, __path__, settings_override)

    # Init assets
    assets.init_app(app)

    # Flask-DebugToolbar
    extensions.debug_toolbar.init_app(app)

    # Flask-Mail
    extensions.mail.init_app(app)

    # Flask-Security
    extensions.security.init_app(app, SQLAlchemyUserDatastore(db, User, Role))

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

