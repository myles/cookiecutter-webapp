# -*- coding: utf-8 -*-
"""
    api.tasks
    {{ "~" * "api.tasks"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: (c) {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask.ext.login import login_required
from flask.ext.restful import Resource, reqparse
from flask.ext.restful import fields, types

from ..models.todos import Todo as TodoModel

req_parser = reqparse.RequestParser()
req_parser.add_argument('title', type=str)
req_parser.add_argument('completed', type=bool)

resource_fields = {
#    'id': fields.Integer,
#    'title': fields.String,
#    'completed': fields.Boolean,
}


class Todo(Resource):

    def get(self, todo_id):
        return TodoModel.get(todo_id).to_dict()

    def put(self, todo_id):
        data = req_parser.parse_args()
        todo = TodoModel.get(todo_id)
        todo.update(**data)
        return todo.to_dict(), 200
        #return '', 204

    def delete(self, todo_id):
        todo = TodoModel.get(todo_id)
        if todo is None:
            return '', 204
        if todo.delete():
            return '', 204
        return {'message': 'Unable to delete'}, 409


class Todos(Resource):

    def get(self):
        #return '', 304, [('ETag', 'bambam')] 
        return [todo.to_dict() for todo in TodoModel.all()]

    def post(self):
        data = req_parser.parse_args()
        todo = TodoModel.create(**data)
        return todo.to_dict(), 201
