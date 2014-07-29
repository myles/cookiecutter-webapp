# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.app_name}}.api
    {{ "~" * (cookiecutter.app_name ~ ".api")|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from . import v1
from .base import ClassyAPI

def create_app(settings_override=None):
    """Returns an API application instance."""

    from .. import framework

    # Create and extend a minimal application
    app = framework.create_app(__name__, __path__, settings_override)

    # Initialize extensions
    app.extensions['classy_api'] = ClassyAPI(app, catch_all_404s=True)

    # Register API versions
    for version in [v1]:
        bp = version.create_blueprint()
        register_blueprint(app, bp)

    return app

def register_blueprint(app, blueprint):
    """Register an API blueprint."""
    if 'classy_api' not in app.extensions:
        raise RuntimeError('ClassyAPI not registered on this application')
    app.extensions['classy_api'].register_blueprint(blueprint)
    app.register_blueprint(blueprint)
