# -*- coding: utf-8 -*-
"""
    api
    ~~~

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask import Blueprint

from .base import ClassyAPI, BaseAPI, BaseResource
from .todos import TodosAPI, TodoResource, TodosResource


def init_api(app):
    """Initialize API to an application"""
    # Create an API blueprint for ClassyAPI views
    # Note: Use a unique blueprint for each API version
    api_v1 = Blueprint("api_v1",  __name__)

    # Initialize Flask-RESTful extensions on the Flask application.
    # We are using Flask-RESTful primarily for the excellent error
    # handling and reqparse features.
    api = ClassyAPI(app)

    # Add Flask-Classy Resources
    TodosAPI.register(api_v1)

    # Add Flask-RESTFul Resources
    # Note: We are registering the Flask-RESTful resources under /api/tasks,
    # not /api/todos to avoid conflicts with TodoAPI's url_rules.
    api.add_resource(TodosResource, '/api/tasks', endpoint='todos_api')
    api.add_resource(TodoResource, '/api/tasks/<int:id>', endpoint='todo_api')

    # Register API blueprints with the Flask application
    app.register_blueprint(api_v1, url_prefix='/api')
    return api
