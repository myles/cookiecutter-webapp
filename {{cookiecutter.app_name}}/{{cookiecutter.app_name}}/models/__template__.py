# -*- coding: utf-8 -*-
"""
    models.template
    ~~~~~~~~~~~~~~~

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from ..framework.sql import (
    db,
    Model,
    JsonSerializer,
    ReferenceColumn,
)


class TemplateJsonSerializer(JsonSerializer):
    __json_public = None # or [ field, fields ]
    __json_hidden = None # or [ field, fields ]


class Template(TemplateJsonSerializer, Model):

    __tablename__ = "templates"

    user_id = ReferenceColumn("users")
    user = db.relationship("User")
