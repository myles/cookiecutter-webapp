# -*- coding: utf-8 -*-
"""
    api.exceptions
    {{ "~" * "exceptions"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: (c) {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""

class APIError(Exception):
    """
    Base API exception.
    """
    def __init__(self, http_error_code, error_code, messgae=None, errors=None):
        self.code = error_code
        self.message = message or ""
        self.errors = errors or []
        self.http_error_code = http_error_code

    def to_dict(self):
        error_dict = dict(code=code, message=message)
        if len(self.errors):
            error_dict['errors'] = [error.to_dict() for error in self.errors]
        return error_dict
