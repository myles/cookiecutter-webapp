# -*- coding: utf-8 -*-
"""
    tests.factories
    {{ "~" * "tests.factories"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from datetime import datetime
from factory import Factory, Sequence, LazyAttribute, PostGenerationMethodCall
from flask.ext.security.utils import encrypt_password

from {{cookiecutter.app_name}}.models.users import User, Role
from {{cookiecutter.app_name}}.models.todos import Todo
from {{cookiecutter.app_name}}.framework.sql import db

class BaseFactory(Factory):
    ABSTRACT_FACTORY = True

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        entity = target_class(**kwargs)
        db.session.add(entity)
        db.session.commit()
        return entity

class RoleFactory(BaseFactory):
    FACTORY_FOR = Role
    name = 'admin'
    description = 'Administrator'

class TodoFactory(BaseFactory):
    FACTORY_FOR = Todo
    title = Sequence(lambda n: "todo #{0}".format(n))

class UserFactory(BaseFactory):
    FACTORY_FOR = User
    email = Sequence(lambda n: 'user{0}@foobar.com'.format(n))
    password = LazyAttribute(lambda a: encrypt_password('password'))
    confirmed_at = datetime.utcnow()
    last_login_at = datetime.utcnow()
    current_login_at = datetime.utcnow()
    last_login_ip = '127.0.0.1'
    current_login_ip = '127.0.0.1'
    login_count = 1
    active = True
