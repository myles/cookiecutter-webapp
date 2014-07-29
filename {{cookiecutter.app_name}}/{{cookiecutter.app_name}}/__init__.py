# -*- coding: utf-8 -*-                                                                                       
"""
    {{ cookiecutter.app_name }}
    {{ "~" * cookiecutter.app_name|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from werkzeug.wsgi import DispatcherMiddleware

from . import api
from . import frontend

def create_app(override_settings=None):
    return DispatcherMiddleware(frontend.create_app(override_settings), {
        '/api': api.create_app(override_settings),
    })

