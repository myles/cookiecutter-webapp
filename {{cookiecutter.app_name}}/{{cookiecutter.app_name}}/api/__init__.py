# -*- coding: utf-8 -*-
"""
    api
    ~~~

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask import Blueprint

from .base import ClassyAPI
from .exceptions import APIError
from .todos import Todo, Todos, TasksAPI


def init_api(app):
    """Initialize API to an application"""

    # Create a versioned API blueprint
    api_blueprint = Blueprint("api",  __name__)

    # Register errorhandlers
    # api_blueprint.errorhandler(APIError)(on_error)

    # Initialize Flask-RESTFul extensions on the API blueprint
    api = ClassyAPI(app)

    # Add Flask-RESTFul Resources
    api.add_resource(Todos, '/api/todos', endpoint='todos_api')
    api.add_resource(Todo, '/api/todos/<int:todo_id>', endpoint='todo_api')

    # Add Flask-Classy Resources
    TasksAPI.register(api_blueprint)

    app.register_blueprint(api_blueprint, url_prefix='/api')
    return api


def on_error(e):
    if isinstance(e, APIError):
        return jsonify(e.to_dict()), e.http_error_code
    return jsonify(
        APIError(500, 911, message="Unknown error raised").to_dict()), 500
