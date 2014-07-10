# -*- coding: utf-8 -*-
"""
    tests.test_models
    {{ "~" * "tests.test_models"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
import pytest

from factory import Sequence
from flask.ext.restless.helpers import to_dict

from {{ cookiecutter.app_name }}.framework.sql import (
    db,
    Model,
    ReferenceColumn,
)

from .factories import BaseFactory

class ApiModel(Model):
    __tablename__ = 'tests'
    __json_hidden__ = ['hidden_attr']

    string_attr = db.Column(db.String(64))
    integer_attr = db.Column(db.Integer)
    hidden_attr = db.Column(db.String(64))

class ApiFactory(BaseFactory):
    FACTORY_FOR = ApiModel

    integer_attr = Sequence(lambda n: n)
    string_attr = Sequence(lambda n: "string {0}".format(n))
    hidden_attr = Sequence(lambda n: "hidden {0}".format(n))

@pytest.mark.usefixtures('db')
class TestModels:

    def test_to_dict(self):
        t = ApiFactory()
        #d = t.to_dict()
        d = to_dict(t, exclude=t.__json_hidden__)
        assert 'integer_attr' in d
        assert 'string_attr' in d
        assert 'hidden_attr' not in d
