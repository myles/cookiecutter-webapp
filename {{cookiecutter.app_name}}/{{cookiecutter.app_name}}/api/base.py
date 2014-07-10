# -*- coding: utf-8 -*-
"""
    api.base
    {{ "~" * "api.base"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask.ext.classy import FlaskView

class APIView(FlaskView):

    model = None
    create_form = None
    update_form = None

    def list(self):
        return self.model.all()

    def create(self):
        form = self.create_form()
        if form.validate_on_submit():
            return self.model.create(**request.json), 201
        raise Exception

    def delete(self, id):
        self.model.get_or_404(id).delete()
        return None, 204

    def patch(self, id):
        return self.update(id)

    def show(self, id):
        return self.model.get_or_404(id)

    def update(self, id):
        form = self.update_form()
        if form.validate_on_submit():
            return self.model.get_or_404(id).update(**request.json)

