# -*- coding: utf-8 -*-
"""
    tests.test_api
    {{ "~" * "tests.test_api"|count }}

    Test API

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
import pytest
from flask import url_for
from flask.ext.security.utils import verify_password

from {{cookiecutter.app_name}}.models.users import User
from .factories import TodoFactory, UserFactory

@pytest.fixture
def user(db):
    return UserFactory(password='myprecious')

@pytest.fixture
def todos(db):
    return [TodoFactory(title='todo #{0}'.format(str(i+1))) for i in range(2)]


class TestAPI:

    def test_not_found(self, testapp):
        resp = testapp.get("/api/some-path-that-does-not-exist", expect_errors=True)
        assert resp.status_code == 404
        assert resp.json['status'] == 404
        assert 'Not Found' in resp.json['message']

    def test_not_found_with_envelope(self, testapp):
        resp = testapp.get("/api/non-existent-path?envelope=true", expect_errors=True)
        assert resp.status_code == 200
        assert resp.json['status'] == 404
        assert 'Not Found' in resp.json['response']['message']

    def test_not_found_with_callback(self, testapp):
        resp = testapp.get("/api/non-existent-path?callback=myfunc", expect_errors=True)
        assert resp.status_code == 200
        assert resp.json['status'] == 404
        assert 'Not Found' in resp.json['response']['message']

    def test_todos_index(self, todos, testapp):
        resp = testapp.get("/api/todos")
        assert isinstance(resp.json, list)
        assert len(resp.json) == 2

    def test_todos_get(self, todos, testapp):
        resp = testapp.get("/api/todos/1")
        assert resp.json['title'] == 'todo #1'
        assert resp.json['completed'] == False

    def test_enveloped_todos_index(self, todos, testapp):
        resp = testapp.get("/api/todos?envelope=true")
        assert isinstance(resp.json, dict)
        assert resp.json['status'] == resp.status_code
        assert len(resp.json['response']) == 2

    def test_unsupported_media(self, testapp):
        """Non-JSON POSTs should fail with a 415 - Unsupported Media Type"""
        resp = testapp.post("/api/todos", {"title": "something"}, expect_errors=True)
        assert resp.status_code == 415
