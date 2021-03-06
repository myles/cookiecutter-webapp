# -*- coding: utf-8 -*-
"""
    tests.conftest
    {{ "~" * "tests.conftest"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.

    templated from https://github.com/ryanolson/cookiecutter-webapp
"""
import pytest
from webtest import TestApp

from {{cookiecutter.app_name}} import api
from {{cookiecutter.app_name}} import frontend
from {{cookiecutter.app_name}}.framework.sql import db as _db

from . import settings as test_settings
from .apis import classy_api, restful_api
from .factories import UserFactory

@pytest.yield_fixture(scope='function')
def app():
    _app = frontend.create_app(test_settings)
    ctx = _app.test_request_context()
    ctx.push()
    yield _app
    ctx.pop()

@pytest.yield_fixture(scope='function', params=['classy', 'restful'])
def apiapp(request):
    _app = api.create_app(test_settings)
    if request.param == 'classy':
        classy_api(_app)
    else:
        restful_api(_app)
    ctx = _app.test_request_context()
    ctx.push()
    yield _app
    ctx.pop()

@pytest.fixture(scope='function')
def testapp(app):
    """A Webtest app."""
    return TestApp(app)

@pytest.fixture(scope='function')
def testapi(apiapp):
    """A Webtest app."""
    return TestApp(apiapp)

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
