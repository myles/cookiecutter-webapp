# -*- coding: utf-8 -*-
"""
    api.base
    {{ "~" * "api.base"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: (c) {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask import request
from flask.ext.classy import FlaskView
from flask.ext.restful import Api as RestfulAPI
from flask.ext.restful import reqparse, types
from flask.ext.restful.representations.json import output_json
from flask.ext.restful.utils import unpack

#get_parser = reqparse.RequestParser()
#get_parser.add_argument('fields', type=str, location='args', store='append')
#get_parser.add_argument('page', type=int, location='args')
#get_parser.add_argument('per_page', type=int, location='args')
#get_parser.add_argument('ETag', type=str, location='headers')

response_options = reqparse.RequestParser()
response_options.add_argument('X-Conditional', type=types.boolean,
                             location='headers')


class ClassyAPI(RestfulAPI):
    """
    Extend Flask-RESTful to play nicely with conditional requests and
    Flask-Classy FlaskViews.
    """

    def owns_endpoint(self, endpoint):
        """
        Extend owns_endpoint to check for a Flask-Classy endpoint that
        inherits from BaseAPI.
        """
        if super(ClassyAPI, self).owns_endpoint(endpoint):
            return True
        if endpoint.startswith('api') and 'API:' in endpoint:
            return True

    def _looks_like_an_api_route(self):
        """
        You know what your API routes should look like.  Customize this
        function with those details.
        """
        path_info = request.environ.get('PATH_INFO', '')
        if path_info.startswith('/api'):
            return True

    def _has_fr_route(self):
        """
        Extends _has_fr_route with a check on if the route looks like
        an API route.
        """
        if super(ClassyAPI, self)._has_fr_route():
            return True
        if self._looks_like_an_api_route():
            return True

    def make_response(self, data, *args, **kwargs):
        """
        If the X-Conditional header evaluates to True, then return a
        conditional GET response, which will return a 304 - Not Modified if the
        ETag in the response matches any of the values in the If-None-Match
        request header, otherwise return the default response.
        """
        resp = super(ClassyAPI, self).make_response(data, *args, **kwargs)
        return conditionalify_response(resp)


class BaseAPI(FlaskView):
    """
    This is the base class from which ClassyAPI FlaskViews should be modeled.
    """
    trailing_slash = None

    def after_request(self, name, response):
        """Conditionalify responses"""
        return conditionalify_response(response)

    @classmethod
    def make_response(cls, response):
        """JSONify responses"""
        return jsonify_response(response)

    @classmethod
    def get_class_suffix(cls):
        """API views will use the -API suffix rather than the -View suffix."""
        return "API"


def jsonify_response(response):
    """
    JSONifies the response with Flask-RESTful's output_json representation.
    """
    data, code, headers = unpack(response)
    response = output_json(data, code, headers)
    response.headers['Content-Type'] = 'application/json'
    return response


def conditionalify_response(response):
    """
    If the X-Conditional header evaluates to True, then return a
    conditional GET response, which will return a 304 - Not Modified if the
    ETag in the response matches any of the values in the If-None-Match
    request header, otherwise return the default response.
    """
    args = response_options.parse_args()
    if request.method == 'GET':
        response.add_etag()
    if args.get('X-Conditional'):
        return response.make_conditional(request)
    return response
