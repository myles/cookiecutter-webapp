# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.app_name }}.frontend.extensions
    {{ "~" * (cookiecutter.app_name ~ ".frontend.extensions")|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.

    templated from https://github.com/ryanolson/cookiecutter-webapp
"""
from ..framework.extensions import *

from flask.ext.debugtoolbar import DebugToolbarExtension
debug_toolbar = DebugToolbarExtension()
