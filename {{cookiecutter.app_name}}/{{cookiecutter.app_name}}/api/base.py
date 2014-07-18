# -*- coding: utf-8 -*-
"""
    api.base
    {{ "~" * "api.base"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: (c) {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask.ext.restful import reqparse

get_parser = reqparse.RequestParser()
get_parser.add_argument('fields', type=str, location='args', store='append')
get_parser.add_argument('page', type=int, location='args')
get_parser.add_argument('per_page', type=int, location='args')
get_parser.add_argument('ETag', type=str, location='headers')

def etag():
    """
    Calculate an ETag value for the data being returned,  Next, check for
    the existance of an If-None-Match header.  If the ETag values matchs
    the value of If-None-Match, return and empty payload with a 304 code.
    Otherwise, add the Etag header to the response.
    """
    pass


