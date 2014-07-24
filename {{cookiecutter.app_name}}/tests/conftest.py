# -*- coding: utf-8 -*-
"""
    tests.conftest
    {{ "~" * "tests.conftest"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
import pytest
from webtest import TestApp

from {{cookiecutter.app_name}}.frontend import create_app
from {{cookiecutter.app_name}}.framework.sql import db as _db

from . import settings as test_settings
from .apis import classy_api, restful_api
from .factories import UserFactory

@pytest.yield_fixture(scope='function')
def app():
    _app = create_app(test_settings)
    ctx = _app.test_request_context()
    ctx.push()
    yield _app
    ctx.pop()

@pytest.fixture(scope='function')
def testapp(app):
    """A Webtest app."""
    return TestApp(app)

@pytest.fixture(scope='function', params=[classy_api, restful_api])
def app_api(app, request):
    request.param(app)
    return TestApp(app)

@pytest.yield_fixture(scope='function')
def db(app):
    _db.app = app
    with app.app_context():
        _db.create_all()
    yield _db
    _db.drop_all()

@pytest.fixture
def user(db):
    return UserFactory()
