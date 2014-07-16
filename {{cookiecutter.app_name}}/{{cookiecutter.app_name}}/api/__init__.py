# -*- coding: utf-8 -*-
"""
    api
    ~~~

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask.ext.restful import Api

from .tasks import Tasks


def init_api(app, url_prefix=None, subdomain=None):
    """Initialize API to an application"""
    api = Api(app, prefix='/api')

    # Map API Resources to Endpoints
    api.add_resource(Tasks, '/tasks', endpoint='tasks_api')

    return api
