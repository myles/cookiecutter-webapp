# -*- coding: utf-8 -*-
"""
    forms.security
    ~~~~~~~~~~~~~~

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask.ext.security.forms import RegisterForm
from ..framework import utils

class ExtendedRegisterForm(RegisterForm):

    def validate(self):
        rv = super(ExtendedRegisterForm, self).validate()
        if not rv:
            utils.flash_errors(self)
        return rv
