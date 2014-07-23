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
    url_prefix = '/api'

    # Initialize Flask-RESTful extensions on the Flask application.
    # We are using Flask-RESTful primarily for the excellent error
    # handling and reqparse features.
    api = ClassyAPI(app)

    # Add Flask-RESTFul Resources
    api.add_resource(Todos, url_prefix + '/todos', endpoint='todos_api')
    api.add_resource(Todo, url_prefix + '/todos/<int:id>', endpoint='todo_api')

    # Create an API blueprint for ClassyAPI views
    # Note: Use multiple blueprints for API versions
    api_v1 = Blueprint("api_v1",  __name__)

    # Add Flask-Classy Resources
    TasksAPI.register(api_v1)

    # Register API blueprints with the Flask application
    app.register_blueprint(api_v1, url_prefix='/api')

    return api
