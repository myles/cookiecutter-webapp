# -*- coding: utf-8 -*-                                                                                       
"""
    api
    ~~~

    :author: {{ cookiecutter.author }}
    :copyright: (c) {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask import Blueprint

from ..framework.core import (
    {{ cookiecutter.AppName }}Error,
    {{ cookiecutter.AppName }}FormError,
)

api = Blueprint('api', __name__)

def init_api(app, url_prefix=None, subdomain=None):
    """Initialize API blueprint"""

    # API blueprint error handlers
    api.errorhandler({{ cookiecutter.AppName }}Error)(on_error)
    api.errorhandler({{ cookiecutter.AppName }}FormError)(on_form_error)
    api.errorhandler(404)(on_404)

    app.json_encoder = JSONEncoder
    app.register_blueprint(api, url_prefix=url_prefix, subdomain=subdomain)
