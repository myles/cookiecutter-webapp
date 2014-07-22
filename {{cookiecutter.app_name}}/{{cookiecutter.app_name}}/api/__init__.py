# -*- coding: utf-8 -*-
"""
    api
    ~~~

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask import Blueprint, jsonify

from .base import API
from .exceptions import APIError
from .todos import Todo, Todos


def init_api(app):
    """Initialize API to an application"""
    url_prefix = '/api'

    # Create a versioned API blueprint
    api_blueprint = Blueprint(url_prefix,  __name__, url_prefix=url_prefix)

    # Register errorhandlers
    api_blueprint.errorhandler(APIError)(on_error)

    # Initialize Flask-RESTFul extensions on the API blueprint
    api = API(api_blueprint)

    # Map API Resources to Endpoints
    api.add_resource(Todos, '/todos', endpoint='todos_api')
    api.add_resource(Todo, '/todos/<int:todo_id>', endpoint='todo_api')

    app.register_blueprint(api_blueprint, url_prefix=url_prefix)
    return api


def on_error(e):
    if isinstance(e, APIError):
        return jsonify(e.to_dict()), e.http_error_code
    return jsonify(
        APIError(500, 911, message="Unknown error raised").to_dict()), 500
