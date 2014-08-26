cookiecutter-webapp
===================

A Flask template for [cookiecutter](https://github.com/audreyr/cookiecutter).


## Requirements
---------------

- [vagrant](http://vagrantup.com)
- [ansible](http://ansible.com)
- [virtualbox](https://www.virtualbox.org/wiki/Downloads)
- [grunt](http://gruntjs.com)
- [bower](http://bower.io)


## Try it now
-------------

```
pip install cookiecutter
cookiecutter https://github.com/ryanolson/cookiecutter-webapp.git
```

You will be asked some basic info about the project you wish to create:

* `app_name`: snake case name of the application
* `AppName`: CamelCase name of the application
* `project_name`: name of your applications, human form
* `license`: choose from `MIT`, `GPLv3`, `GPLv2`, `Apache`, `ISC`, `Mozilla`
  ** you can write in any string here; however you will need to provide the
     details for the LICENSE file
* `author`
* `email`
* `company`
* `copyright`: usually takes the form of "Year, Company/Author"
   ** note: © prepended
* `app_repo`: git repository for storing your code
* `app_url`: the url for the hosted project
* `vagrant_ipv4`: the host-only IP address for the vagrant-managed virtual
   machine that will be created and provisioned. 

```
npm install
grunt
vagrant up
```

After Vagrant and Ansible do their work, direct your browser to
`https://192.168.100.10` or whatever IP address you specifed for `vagrant_ipv4`.

Read the README.md file created in your project directory for more details on
development, testing and deployment.


## Features
-----------

-   Vagrant to bring up a local development server
-   Ansible for provisioning
-   Flask WSGI application
-   Grunt and Bower to manage web assets
-   Stateless RESTful API
-   Flask-SQLAlchemy with basic User model
-   Secure logins via Flask-Security, Flask-WTForms
-   Easy database migrations with Flask-Migrate
-   Bootstrap 3 and Font Awesome 4 with starter templates
-   CSS and JS minification using Flask-Assets
-   Caching using Flask-Cache
-   pytest, WebTest, and Factory-Boy for testing
-   A simple Flask-Script `manage.py` script.
-   Useful debug toolbar
-   Utilizes best practices:
    [Blueprints](http://flask.pocoo.org/docs/blueprints/) and
    [Application
    Factory](http://flask.pocoo.org/docs/patterns/appfactories/)
    patterns


## Inspiration
---------------

-   [How I Structure My Flask
    Applications](http://mattupstate.com/python/2013/06/26/how-i-structure-my-flask-applications.html)
    by Matt Wright
-   [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask/)
    by Steven Loria


## Good Reads
-------------

-   [Optimizing RequireJS
    applications](http://www.webdeveasy.com/optimize-requirejs-projects/)


## License
----------

MIT licensed.


## Major TODOs
--------------


## Changelog
------------

### 0.1.0 (07/01/2014)
* first iteration - in development

