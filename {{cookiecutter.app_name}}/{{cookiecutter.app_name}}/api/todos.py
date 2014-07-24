# -*- coding: utf-8 -*-
"""
    api.todos
    {{ "~" * "api.todos"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: (c) {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask.ext.login import login_required
from flask.ext.restful import abort, reqparse

from .base import BaseAPI, BaseResource
from ..models.todos import Todo

todo_parser = reqparse.RequestParser()
todo_parser.add_argument('title', type=str)
todo_parser.add_argument('completed', type=bool)


class TodosAPI(BaseAPI):
    """A complete Flask-Classy-based Todo API resource."""

    def index(self):
        """Returns a Collection of Todos."""
        return [todo.to_dict() for todo in Todo.all()]

    def post(self):
        """Creates a new Todo."""
        data = todo_parser.parse_args()
        todo = Todo.create(**data)
        return todo.to_dict(), 201

    def get(self, id):
        """Returns a specific of Todo."""
        return Todo.get(id).to_dict()

    def put(self, id):
        """Updates an existing Todo."""
        data = todo_parser.parse_args()
        todo = Todo.get(id)
        todo.update(**data)
        return todo.to_dict(), 200
        #return '', 204

    def delete(self, id):
        """Deletes an existing Todo."""
        todo = Todo.get(id)
        if todo is None:
            return '', 204
        if todo.delete():
            return '', 204
        abort(409)


class TodosResource(BaseResource):
    """Flask-RESTful-based Todo API Resource for GET, POST."""

    def get(self):
        """Returns a Collection of Todos."""
        return [todo.to_dict() for todo in Todo.all()]

    def post(self):
        """Creates a new Todo."""
        data = todo_parser.parse_args()
        todo = Todo.create(**data)
        return todo.to_dict(), 201


class TodoResource(BaseResource):
    """Flask-RESTful-based Todo API Resource for GET, PUT and DELETE."""

    def get(self, id):
        """Returns a specific of Todo."""
        return Todo.get(id).to_dict()

    def put(self, id):
        """Updates an existing Todo."""
        data = todo_parser.parse_args()
        todo = Todo.get(id)
        todo.update(**data)
        return todo.to_dict(), 200
        #return '', 204

    def delete(self, id):
        """Deletes an existing Todo."""
        todo = Todo.get(id)
        if todo is None:
            return '', 204
        if todo.delete():
            return '', 204
        abort(409)
