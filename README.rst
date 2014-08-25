cookiecutter-webapp
===================

A Flask template for cookiecutter_.

.. _cookiecutter: https://github.com/audreyr/cookiecutter


Requirements
------------

- `vagrant <http://vagrantup.com>`_
- `ansible <http://ansible.com>`_
- `grunt <http://gruntjs.com>`_
- `bower <http://bower.io>`_


Use it now
----------
::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/ryanolson/cookiecutter-webapp.git

You will be asked about your basic info (name, project name, app name, etc.). This
info will be used to generate your new project.

::

    $ npm install
    $ grunt
    $ vagrant up

Features
--------

- Vagrant to bring up a local development server
- Ansible for provisioning
- Flask WSGI application
- Grunt and Bower to manage web assets
- Stateless RESTful API
- Flask-SQLAlchemy with basic User model
- Secure logins via Flask-Security, Flask-WTForms
- Easy database migrations with Flask-Migrate
- Bootstrap 3 and Font Awesome 4 with starter templates
- CSS and JS minification using Flask-Assets
- Caching using Flask-Cache
- pytest, WebTest, and Factory-Boy for testing
- A simple Flask-Script ``manage.py`` script.
- Useful debug toolbar
- Utilizes best practices: `Blueprints <http://flask.pocoo.org/docs/blueprints/>`_ and `Application Factory <http://flask.pocoo.org/docs/patterns/appfactories/>`_ patterns


Screenshots
-----------

.. image:: https://dl.dropboxusercontent.com/u/1693233/github/cookiecutter-flask-01.png
    :target: https://dl.dropboxusercontent.com/u/1693233/github/cookiecutter-flask-01.png
    :alt: Home page

.. image:: https://dl.dropboxusercontent.com/u/1693233/github/cookiecutter-flask-02.png.png
    :target: https://dl.dropboxusercontent.com/u/1693233/github/cookiecutter-flask-02.png.png
    :alt: Registration form



Inspiration
-----------

- `How I Structure My Flask Applications <http://mattupstate.com/python/2013/06/26/how-i-structure-my-flask-applications.html>`_ by Matt Wright
- `cookiecutter-flask <https://github.com/sloria/cookiecutter-flask/>`_ by Steven Loria
- `Flask Official Documentation <http://flask.pocoo.org/docs/>`_

Optimization
------------
- `Optimizing RequireJS applications <http://www.webdeveasy.com/optimize-requirejs-projects/>`_

License
-------

MIT licensed.


Major TODOs
-----------



Changelog
---------

0.1.0 (07/01/2014)
******************

- first iteration
