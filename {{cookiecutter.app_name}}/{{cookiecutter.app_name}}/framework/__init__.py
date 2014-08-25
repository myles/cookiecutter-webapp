# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.app_name }}.framework
    {{ "~" * (cookiecutter.app_name ~ ".framework")|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.

    templated from https://github.com/ryanolson/cookiecutter-webapp
"""
from .factory import create_app
from .utils import flash_errors, generate_salt
