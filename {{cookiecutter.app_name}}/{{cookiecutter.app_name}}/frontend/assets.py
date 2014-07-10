# -*- coding: utf-8 -*-                                                                                       
"""
    frontend.assets
    ~~~~~~~~~~~~~~~

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
import os
from flask.ext.assets import Bundle, Environment

root_directory = os.path.dirname(os.path.abspath(__file__))
assets_directory = os.path.join(root_directory, 'assets')
bower_directory = os.path.join(root_directory, 'static')

css_complete = Bundle(
    "css/bootstrap.css",
    "css/font-awesome.css",
    "css/{{ cookiecutter.app_name }}.css",
    filters="cssmin",
    output="css/bundled/{{ cookiecutter.app_name }}_complete.css"
)

css_no_vendor = Bundle(
    "css/{{ cookiecutter.app_name }}.css",
    filters="cssmin",
    output="css/bundled/{{ cookiecutter.app_name }}.css"
)

js_shiv = Bundle(
    "js/html5shiv.js",
    "js/respond.js",
    filters="jsmin",
    output="js/bundled/shiv.js"
)

js_top = Bundle(
    "js/modernizr.js",
    filters="jsmin",
    output="js/bundled/top.js"
)

js_application = Bundle(
    "coffee/{{ cookiecutter.app_name }}.coffee",
    filters="coffeescript",
)

js_complete = Bundle(
    "js/jquery.js",
    "js/pjax.js",
    "js/bootstrap.min.js",
    js_application,
    filters="jsmin",
    output="js/bundled/{{ cookiecutter.app_name}}_complete.js"
)

js_no_vendor = Bundle(
    js_application,
    filters="jsmin",
    output="js/bundled/{{ cookiecutter.app_name}}.js"
)


def init_app(app):
    assets = Environment(app)
    assets.directory = app.static_folder
    assets.url = app.static_url_path
    assets.directory = app.static_folder
    assets.append_path(assets_directory)
    assets.append_path(bower_directory)
    assets.register("css_complete", css_complete)
    assets.register("css_no_vendor", css_no_vendor)
    assets.register("js_application", js_application)
    assets.register("js_complete", js_complete)
    assets.register("js_no_vendor", js_no_vendor)
    assets.register("js_shiv", js_shiv)
    assets.register("js_top", js_top)
