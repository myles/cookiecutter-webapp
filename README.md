cookiecutter-webapp
===================

A Flask template for [cookiecutter](https://github.com/audreyr/cookiecutter).


## Requirements

- [vagrant](http://vagrantup.com)
- [ansible](http://ansible.com)
- [virtualbox](https://www.virtualbox.org/wiki/Downloads)
- [grunt](http://gruntjs.com)
- [bower](http://bower.io)


## Try it now

```
pip install cookiecutter
cookiecutter https://github.com/ryanolson/cookiecutter-webapp.git
```

You will be asked some basic info about the project you wish to create:

- `app_name`: snake case name of the application
- `AppName`: CamelCase name of the application
- `project_name`: name of your applications, human form
- `license`
    * `MIT`
    * `GPLv3`
    * `GPLv2`
    * `Apache`
    * `ISC`
    * `Mozilla`
    * any other license - you will have to add the text to the LICENSE file
- `author`
- `email`
- `company`
- `copyright`: usually takes the form of "Year, Company/Author" (@ will be prepended)
- `app_repo`: git repository for storing your code
- `app_url`: the url for the hosted project
- `vagrant_ipv4`: the host-only IP address for the vagrant-managed virtual
   machine that will be created and provisioned. 

Next, change directories to your newly created `app_name` project directory

```
npm install
grunt
vagrant up
```

Note: you might get an error on `npm install` where some of the dependencies want an
earlier version of grunt.  Try the `grunt` command and if all goes well, you are on
your way to `vagrant up`.

After Vagrant and Ansible do their work, direct your browser to
`https://192.168.100.10` or whatever IP address you specifed for `vagrant_ipv4`.

Read the README.md file created in your project directory for more details on
development, testing and deployment.


## Features

- [Vagrant](http://vagrantup.com) to bring up a local development server
- [Ansible](http://ansible.com) for provisioning
- [Flask](https://github.com/mitsuhiko/flask) WSGI application
- [Grunt](http://gruntjs.com) and [Bower](http://bower.io) to manage web assets
- [Pragmatic Stateless RESTful API](http://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)
  using a combination of [Flask-Classy](https://github.com/apiguy/flask-classy) and
  [Flask-RESTful](https://github.com/twilio/flask-restful).
- Dynamic user interface based on [React](http://facebook.github.io/react/) and
  [Backbone.JS](http://backbonejs.org)
- [Flask-SQLAlchemy](https://github.com/mitsuhiko/flask-sqlalchemy) with basic User model
- Secure logins via [Flask-Security](https://github.com/mattupstate/flask-security),
  [Flask-WTForms](https://github.com/lepture/flask-wtf)
- Easy database migrations with [Flask-Migrate](https://github.com/miguelgrinberg/Flask-Migrate)
- [Twitter's Bootstrap 3](http://getbootstrap.com) and
  [Font Awesome 4](http://fortawesome.github.io/Font-Awesome/)
- [pytest](http://pytest.org/latest/),
  [WebTest](http://webtest.readthedocs.org/en/latest/), and
  [Factory-Boy](http://factoryboy.readthedocs.org/en/latest/) for testing
- A simple [Flask-Script](https://github.com/smurfix/flask-script) `manage.py` script.
- Useful [debug toolbar](https://github.com/mgood/flask-debugtoolbar)


## Inspiration

- [Best Practices for Designing a Pragmatic RESTful API](http://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api) by Vinay Sahni
- [How I Structure My Flask
  Applications](http://mattupstate.com/python/2013/06/26/how-i-structure-my-flask-applications.html)
  by Matt Wright
- [Flask/WSGI Application Deployment using Ubuntu, Ansible, Nginx, Supervisor and uWSGI](http://mattupstate.com/python/devops/2012/08/07/flask-wsgi-application-deployment-with-ubuntu-ansible-nginx-supervisor-and-uwsgi.html)
- [Multi Server Flask Application Development Environment with Vagrant and Ansible](http://mattupstate.com/python/devops/2012/08/30/multi-server-flask-application-development-enviornment-with-vagrant-and-ansible.html)
- [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask/)
  by Steven Loria


## Good Reads

-   [Optimizing RequireJS
    applications](http://www.webdeveasy.com/optimize-requirejs-projects/)


## License

MIT licensed.


## Major TODOs


## Changelog

### 0.1.0 (07/01/2014)
* first iteration - in development

