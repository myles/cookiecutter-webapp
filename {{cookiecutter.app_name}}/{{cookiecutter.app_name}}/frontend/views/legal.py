# -*- coding: utf-8 -*-
"""
    frontend.views.legal
    {{ "~" * "frontend.views.legal"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""

from flask import render_template
from flask.ext.classy import FlaskView

class LegalView(FlaskView):

    def privacy(self):
        return render_template("legal/privacy.html")

    def terms_of_use(self):
        return render_template("legal/terms_of_use.html")
