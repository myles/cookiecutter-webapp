# -*- coding: utf-8 -*-                                                                                       
"""
    frontend.views
    ~~~~~~~~~~~~~~

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from .legal import LegalView
from .todo import TodoView

def init_app(app):
    LegalView.register(app)
    TodoView.register(app)
