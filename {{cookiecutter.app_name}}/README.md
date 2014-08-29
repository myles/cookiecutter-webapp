{{ "=" * cookiecutter.project_name|count }}
{{ cookiecutter.project_name }}
{{ "=" * cookiecutter.project_name|count }}

## Quickstart

```
vagrant up
```

## Virtual Machine and Provisioning

### Vagrant

Vagrant maps your local project directory (the directory containing
`Vagrantfile`) to `/vagrant` directory on the provisioned VM. Any changes to
the project directory on your local machine are immediately seen by the VM
server.

`vagrant ssh` will log you into the VM.

`vagrant provision` will reprovision the VM.

Typically, when you work on the development VM directly, you will do the following:

```
vagrant ssh
source /srv/webapps/{{ cookiecutter.app_name }}/venv/bin/activate
cd /vagrant
```

All commands run on the VM will have assumed you have logged in using the above
commands.


### Ansible

To execute ansible commands/playbooks, you need to be able to ssh into the VM
via the `ssh` command.  Check your SSH agent keychains to ensure Vagrant's
`insecure_private_key` has been loaded with `ssh-add -L`.  You can add
Vagrant's `insecure_private_key` by executing the following:

```
ssh-add ~/.vagrant.d/insecure_private_key
```

To provision using Ansible directly, do the following:

```
ansible-playbook develop.yml -u vagrant -i ./hosts
```

You can use the `--tags` options to limit what you want to reprovision.  This is
useful when you do not want to run the whole playbook.


## {{ cookiecutter.app_name }} development

You can develop in three different modes:

- using the VM entirely
- using a combination of the VM to run the various backend services (PostgreSQL,
  Redis, etc.) while the local machine is used run the Flask webapp.
- local machine entirely -- all components are run on the local machine


### Components

There are two primary development components:

- Python / Jinja / server-side code
- Coffeescript / React / Backbone / client-side code

#### Flask: Python / Jinja

After provisioning, the Flask web application is run by Gunicorn which is
controlled by Supervisor. Gunicorn is run using the `--reload` option when
`app_debug=True`. Modifications to any `.py` files in the project directory
should cause gunicorn to reload the webapp. If you see nginx reporting
`502 Bad Gateway` errors, it is likely you have some syntax errors that cause
the webapp to fail to load.

To run the {{ cookiecutter.app_name }} manually, simply log into the VM as
described above and run:

```
python manage.py server
```

To access this manual version, direct your browser to
<http://192.168.100.10:5000>. Using this method, you will bypass nginx and the
supervisor controlled gunicorn instance.  

To manually restart the Gunicorn/Supervisor instance:

```
sudo supervisorctl restart {{ cookiecutter.app_name }}
```

The Flask web application can also be run directly on your local
machine using `python manage.py server`.  While the webapp is run locally, you can
still use the VM backend services such as PostgreSQL, Redis, etc. by setting the
`{{ cookiecutter.app_name|upper }}_INSTANCE_PATH` to fullpath for `instance-vagrant`
in the project directory (created by ansible provisioning on the VM).

##### Hybrid development (VM+local)

If you wish to run the webapp on your local machine using services on the VM,
you will need to:

1. create a virtualenv and install the development requirements:
   `pip install -r requirements/develop.txt`
2. set the environmental variable {{ cookiecutter.app_name|upper }}_INSTANCE_PATH
   to the full path of the `instance-vagrant` directory in your top-level path
    * `instance-vagrant` will be created during the initial provisioning
    * the vm must be running
3. use `python manage.py server` to start the webapp on your machine

##### Local-only development

Not all options may be available with local-only development.  Note, this options
does not share the database on the VM. 

1. create a virtualenv and install the development requirements:
   `pip install -r requirements/develop.txt`
2. create the local sql db: `python manage.py db upgrade`
3. use `python manage.py server` to start the webapp on your machine


#### Coffeescript -> Javascript: Backbone + React

The Javascript client-side code is compiled from Coffeescript with packages
installed via Node/npm.  The development VM is provisioned with Node and the
require packages.

The initial provisioning executes `grunt` which updates bower, copies web assets
to the desired location, and compiles all coffeescript sources.

During development, you will need to either run `grunt` to manually update any
changes you make, or run `grunt watch` which will monitor your coffeescript
files and recompile them when they are modified.

Grunt can be run on either your local machine or the development VM.  Here
is an example of running Grunt on the VM after logging in as described above.

```
grunt watch
```


## Running Tests

Similar to developing, you can run tests either locally on your machine or on the
VM.

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
