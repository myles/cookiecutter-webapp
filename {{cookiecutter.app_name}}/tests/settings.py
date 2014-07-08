# -*- coding: utf-8 -*-
"""
    tests.settings
    {{ "~" * "tests.settings"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: (c) {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""

DEBUG = False
TESTING = True
SECRET_KEY = 'testing-secret-key'

CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS=True
BROKER_BACKEND='memory'

SQLALCHEMY_POOL_SIZE = None
SQLALCHEMY_POOL_TIMEOUT = None
SQLALCHEMY_POOL_RECYCLE = None
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

SECURITY_PASSWORD_HASH = 'plaintext'
SECURITY_CONFIRMABLE = False
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = False
SECURITY_CHANGEABLE = True
SECURITY_TRACKABLE = True
SECURITY_FLASH_MESSAGES = True
SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
