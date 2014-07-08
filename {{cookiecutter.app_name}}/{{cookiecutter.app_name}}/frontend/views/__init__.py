# -*- coding: utf-8 -*-                                                                                       
"""
    frontend.views
    ~~~~~~~~~~~~~~

    :author: {{ cookiecutter.author }}
    :copyright: (c) {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from .checklist import ChecklistView
from .legal import LegalView

def init_app(app):
    ChecklistView.register(app)
    LegalView.register(app)
