# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.app_name }}.api.v1
    {{ "~" * (cookiecutter.app_name ~ ".api.v1")|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from .todos import TodosAPI, TodosResource, TodoResource

def create_blueprint(name=None, url_prefix=None, subdomain=None):
    """Register API endpoints on a Flask :class:`Blueprint`."""

    from flask import Blueprint

    # Determine blueprint name
    name = name or __name__.split('.')[-1]
    url_prefix = url_prefix or "/{0}".format(name)
    if subdomain:
        name = "{0}_{1}".format(subdomain, name)

    # Create blueprint
    bp = Blueprint(name, __name__, url_prefix=url_prefix, subdomain=subdomain)

    # Register API endpoints
    TodosAPI.register(bp)

    return bp
