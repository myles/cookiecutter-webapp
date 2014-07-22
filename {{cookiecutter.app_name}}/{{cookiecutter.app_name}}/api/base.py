# -*- coding: utf-8 -*-
"""
    api.base
    {{ "~" * "api.base"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: (c) {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
import functools
from flask import request
from flask.ext.restful import Api as BaseAPI
from flask.ext.restful import reqparse, types

#get_parser = reqparse.RequestParser()
#get_parser.add_argument('fields', type=str, location='args', store='append')
#get_parser.add_argument('page', type=int, location='args')
#get_parser.add_argument('per_page', type=int, location='args')
#get_parser.add_argument('ETag', type=str, location='headers')

resp_parser = reqparse.RequestParser()
resp_parser.add_argument('X-Conditional',
                         type=types.boolean, location='headers')


class API(BaseAPI):
    """
    Extend Flask-RESTful to play nicely with conditional requests.
    """

    def make_response(self, data, *args, **kwargs):
        """
        If the X-Conditional header evaluates to True, then return a
        conditional GET response, which will return a 304 - Not Modified if the
        ETag in the response matches any of the values in the If-None-Match
        request header, otherwise return the default response.
        """
        resp = super(API, self).make_response(data, *args, **kwargs)
        args = resp_parser.parse_args()
        if request.method == 'GET':
            resp.add_etag()
        if args.get('X-Conditional'):
            return resp.make_conditional(request)
        return resp
