# -*- coding: utf-8 -*-
"""
    tests.test_api
    {{ "~" * "tests.test_api"|count }}

    Test API

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
import copy
import pytest

from .factories import TodoFactory

@pytest.fixture
def user(db):
    return UserFactory(password='myprecious')

@pytest.fixture
def todos(db):
    return [TodoFactory(title='todo #{0}'.format(str(i+1))) for i in range(2)]


class TestAPI:
    """
    Tests both Flask-Classy and Flask-RESTful based APIs.  The `app_api` fixture
    will test each test function twice: `api_app0`==Classy, `api_app1`==RESTful.
    """

    def test_not_found(self, app_api):
        resp = app_api.get("/api/some-path-that-does-not-exist", expect_errors=True)
        assert resp.status_code == 404
        assert resp.json['status'] == 404
        assert 'Not Found' in resp.json['message']

    def test_not_found_with_envelope(self, app_api):
        resp = app_api.get("/api/non-existent-path?envelope=true", expect_errors=True)
        assert resp.status_code == 200
        assert resp.json['status'] == 404
        assert 'Not Found' in resp.json['response']['message']

    def test_not_found_with_callback(self, app_api):
        resp = app_api.get("/api/non-existent-path?callback=myfunc", expect_errors=True)
        assert resp.status_code == 200
        assert resp.json['status'] == 404
        assert 'Not Found' in resp.json['response']['message']

    def test_todos_index(self, todos, app_api):
        resp = app_api.get("/api/tests/todos")
        assert isinstance(resp.json, list)
        assert len(resp.json) == 2

    def test_todos_post(self, db, app_api):
        resp = app_api.post_json("/api/tests/todos", {"title": "todo #1"})
        assert resp.status_code == 201
        assert 'id' in resp.json

    def test_todos_get(self, todos, app_api):
        resp = app_api.get("/api/tests/todos/1")
        assert resp.json['title'] == 'todo #1'
        assert resp.json['completed'] == False

    def test_todos_put(self, db, app_api):
        resp = app_api.post_json("/api/tests/todos", {"title": "todo #1"})
        assert resp.status_code == 201
        assert 'id' in resp.json
        data = copy.copy(resp.json)
        data['completed'] = True
        uri = "/api/tests/todos/{0}".format(resp.json['id'])
        resp = app_api.put_json(uri, data)
        assert resp.status_code == 200
        assert resp.json['completed'] == True

    def test_todos_delete(self, todos, app_api):
        resp = app_api.delete("/api/tests/todos/{0}".format(todos[0].id))
        resp.status_code == 204
        resp = app_api.delete_json("/api/tests/todos/{0}".format(todos[0].id))
        resp.status_code == 204

    def test_todos_patch(self, todos, app_api):
        uri = "/api/tests/todos/{0}".format(todos[0].id)
        resp = app_api.patch_json(uri, {"completed": True}, expect_errors=True)
        assert resp.status_code == 405

    def test_unsupported_media(self, app_api):
        """Non-JSON POSTs should fail with a 415 - Unsupported Media Type"""
        resp = app_api.post("/api/tests/todos", {"title": "something"},
                            expect_errors=True)
        assert resp.status_code == 415

    def test_enveloped_todos_index(self, todos, app_api):
        resp = app_api.get("/api/tests/todos?envelope=true")
        assert isinstance(resp.json, dict)
        assert resp.json['status'] == resp.status_code
        assert len(resp.json['response']) == 2

