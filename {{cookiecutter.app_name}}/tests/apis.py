# -*- coding: utf-8 -*-
"""
    test.apis
    {{ "~" * "test.apis"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: (c) {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask import Blueprint
from {{ cookiecutter.app_name }}.api import ClassyAPI
from {{ cookiecutter.app_name }}.api import TodosAPI, TodosResource, TodoResource

def classy_api(app):
    """Create an Flask-Classy-based API on app"""
    api_bp = Blueprint("api_tests", __name__)
    api_ext = ClassyAPI(app)
    TodosAPI.register(api_bp)
    app.register_blueprint(api_bp, url_prefix='/api/tests')


def restful_api(app):
    """Create an Flask-RESTful-based API on app"""
    api_ext = ClassyAPI(app)
    api_ext.add_resource(TodosResource, '/api/tests/todos', endpoint='todos_api')
    api_ext.add_resource(TodoResource, '/api/tests/todos/<int:id>', endpoint='todo_api')
