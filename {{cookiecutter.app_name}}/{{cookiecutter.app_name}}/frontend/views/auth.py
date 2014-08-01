# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.app_name }}.frontend.security
    {{ "~" * (cookiecutter.app_name ~ ".frontend.security")|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask import current_app, jsonify, request
from flask.ext.classy import FlaskView, route
from flask.ext.jwt import generate_token
from flask.ext.restful.reqparse import RequestParser
from flask.ext.security import current_user

request_options = RequestParser()
request_options.add_argument('Content-Type', type=str, location='headers')

class AuthView(FlaskView):

    @route('/jwt/token', methods=['POST'])
    def jwt_token(self):
        """
        Returns a JWT token if the user is logged in and the post has
        content type application/json.  All errors are returned as json.
        """
        if not current_user.is_authenticated():
            return jsonify({
                "status": 403,
                "message": "No user authenticated",
            }), 403
        options = request_options.parse_args()
        content_json = options.get('Content-Type') == 'application/json'
        if not content_json:
            return jsonify({
                "status": 415,
                "message": "Unsupported media type",
            }), 415
        return jsonify(dict(token=generate_token(current_user)))
