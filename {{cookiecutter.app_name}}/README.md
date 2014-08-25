{{ "=" * cookiecutter.project_name|count }}
{{ cookiecutter.project_name }}
{{ "=" * cookiecutter.project_name|count }}

## Quickstart

```
npm install
grunt
vagrant up
```

## Local Development

1) Create and load a virtualenv
2) `pip install -r requirements/develop.txt`


### Shell

To open the interactive shell, run :

```
python manage.py shell
```

By default, you will have access to:
  * `app`: `werkzeug.wsgi.DispatcherMiddleware` for combining multiple WSGI
     applications
  * `frontend`: `<Flask '{{ cookiecutter.app_name }}.frontend'>`
  * `api`: `<Flask '{{ cookiecutter.app_name }}.api'>`
  * `db`: `<SQLAlchemy engine='sqlite:////tmp/{{ cookiecutter.app_name }}.db'>`
  * `User`: `<class '{{ cookiecutter.app_name }}.models.users.User'>`

### Running Tests

To run all tests, run :

```
py.test
```

### Migrations

Whenever a database migration needs to be made. Run the following
commmands:

```
python manage.py db migrate
```

This will generate a new migration script.  Then run:

```
python manage.py db upgrade
```

To apply the migration.

For a full migration command reference, run
`python manage.py db --help`.
