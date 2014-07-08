{{ "=" * cookiecutter.project_name|count }}
{{ cookiecutter.project_name }}
{{ "=" * cookiecutter.project_name|count }}


Quickstart
----------

::

    mkvirtualenv {{ cookiecutter.app_name }}
    pip install -r requirements/develop.txt
    bower install
    npm install
    grunt
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py server


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``db``, and the ``User`` model.


Running Tests
-------------

To run all tests, run ::

    python manage.py test


Migrations
----------

Whenever a database migration needs to be made. Run the following commmands:
::

    python manage.py db migrate

This will generate a new migration script. Then run:
::

    python manage.py db upgrade

To apply the migration.

For a full migration command reference, run ``python manage.py db --help``.
