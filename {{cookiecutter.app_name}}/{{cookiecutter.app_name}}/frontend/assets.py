# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.app_name }}.frontend.assets
    {{ "~" * (cookiecutter.app_name ~ ".frontend.assets")|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.

    templated from https://github.com/ryanolson/cookiecutter-webapp
"""
import os
from flask.ext.assets import Bundle, Environment

root_directory = os.path.dirname(os.path.abspath(__file__))
assets_directory = os.path.join(root_directory, 'client')
bower_directory = os.path.join(root_directory, 'static')

h5bp_css = Bundle(
    "css/vendor/bootstrap.css",
    "css/vendor/font-awesome.css",
    "css/{{ cookiecutter.app_name }}.css",
    filters="cssmin",
    output="css/{{ cookiecutter.app_name }}.min.css"
)

h5bp_shiv = Bundle(
    "js/vendor/html5shiv.js",
    "js/vendor/respond.js",
    filters="jsmin",
    output="js/bundled/shiv.js"
)

h5bp_head_js = Bundle(
    "js/vendor/modernizr.js",
    filters="jsmin",
    output="js/head.min.js"
)

h5bp_body_js_devel = Bundle(
    "js/vendor/require.js",
    filters="jsmin",
    output="js/develop.min.js"
)

h5bp_body_js_production = Bundle(
    "js/vendor/require.js",
    filters="jsmin",
    output="js/{{ cookiecutter.app_name }}.min.js"
)

def init_app(app):
    assets = Environment(app)
    assets.debug = app.config.get('DEBUG', False)
    assets.directory = app.static_folder
    assets.url = app.static_url_path
    assets.directory = app.static_folder
    assets.append_path(assets_directory)
    assets.append_path(app.static_folder)
    assets.register("h5bp_css", h5bp_css)
    assets.register("h5bp_shiv", h5bp_shiv)
    assets.register("h5bp_head_js", h5bp_head_js)
    if assets.debug:
        assets.register("h5bp_body_js", h5bp_body_js_devel)
    else:
        assets.register("h5bp_body_js", h5bp_body_js_production)
