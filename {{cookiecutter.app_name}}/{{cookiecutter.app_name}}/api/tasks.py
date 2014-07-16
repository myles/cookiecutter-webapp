# -*- coding: utf-8 -*-
"""
    api.tasks
    {{ "~" * "api.tasks"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: (c) {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask.ext.restful import Resource

TASKS = {'tasks': [
    {
        "title": "something",
        "completed": False,
    },
    {
        "title": "something else",
        "completed": False,
    },
    {
        "title": "this",
        "completed": False,
    },
    {
        "title": "that",
        "completed": False,
    },
    {
        "title": "another thing",
        "completed": False,
    },
]}


class Tasks(Resource):
    def get(self):
        return TASKS
