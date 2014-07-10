# -*- coding: utf-8 -*-
"""
    tasks.workq
    {{ "~" * "tasks.workq"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from ..framework.factory import create_celery_app
celery = create_celery_app()
task = celery.task
