# -*- coding: utf-8 -*-
"""
    extensions.py
    ~~~~~~~~~~~~~

    Initialize Frontend Flask and Jinja extensions.

    :authro: {{ cookiecutter.author }}
    :copyright: (c) {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask.ext.debugtoolbar import DebugToolbarExtension
debug_toolbar = DebugToolbarExtension()
