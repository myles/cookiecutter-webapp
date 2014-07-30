# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.app_name }}.models.todos
    {{ "~" * (cookiecutter.app_name ~ ".models.todos")|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from ..framework.sql import (
    db,
    Model,
    ReferenceColumn,
)


class Todo(Model):

    __tablename__ = "todos"

    title = db.Column(db.String(128), nullable=False)
    completed = db.Column(db.Boolean, default=False)

