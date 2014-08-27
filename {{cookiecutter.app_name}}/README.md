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

You can develop locally in three different modes:

- using the VM entirely
- using a combination of the VM to run the various backend services while
  the local machine is used run the webapp.
- local machine entirely

In either case, you need to run `grunt watch` locally to watch and recompile
any modifications to coffeescript files.

### VM-only development

Gunicorn is run using the `--reload` option when the VM is provisioned with
`app_debug=True`.  Modifications to any `.py` file should cause gunicorn to
reload the webapp.  If you see nginx reporting `502 Bad Gateway` errors, it
is likely you have some syntax errors that cause the webapp to fail to load.

### Hybrid development (VM+local)

If you wish to run the webapp on your machine using services on the VM,
you will need to:

1. create a virtualenv and install the development requirements:
   `pip install -r requirements/develop.txt`
2. set the environmental variable {{ cookiecutter.app_name|upper }}_INSTANCE_PATH
   to the full path of the `instance-vagrant` directory in your top-level path
    * `instance-vagrant` will be created during the initial provisioning
    * the vm must be running
3. use `python manage.py server` to start the webapp on your machine

### Local-only development

Not all options may be available with local-only development.  Note, this options
does not share the database on the VM. 

1. create a virtualenv and install the development requirements:
   `pip install -r requirements/develop.txt`
2. create the local sql db: `python manage.py db upgrade`
3. use `python manage.py server` to start the webapp on your machine


## Running Tests

To run all tests, run :

```
python manage test
```

or

```
py.test
```


## DB Migrations

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

## Shell

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
