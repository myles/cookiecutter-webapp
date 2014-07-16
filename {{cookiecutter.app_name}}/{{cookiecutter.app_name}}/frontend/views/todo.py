# -*- coding: utf-8 -*-
"""
    frontend.views.todo
    {{ "~" * "frontend.views.todo"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask import render_template #, redirect, current_app, url_for, request
from flask import flash
from flask.ext.classy import FlaskView
from flask.ext.login import login_required
from werkzeug.local import LocalProxy
# from werkzeug.datastructures import MultiDict

# Extensions
_security = LocalProxy(lambda: current_app.extensions['security'])
# _social = LocalProxy(lambda: current_app.extensions['social'])

class TodoView(FlaskView):
    route_base = '/'

    def index(self):
        return render_template("views/todo/index.html")

    @login_required
    def secret(self):
        flash("super secret message", category='info')
        return render_template("views/todo/index.html")
