# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.app_name }}.frontend.extensions
    {{ "~" * (cookiecutter.app_name ~ ".frontend.extensions")|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from ..framework.extensions import *

from flask.ext.debugtoolbar import DebugToolbarExtension
debug_toolbar = DebugToolbarExtension()
