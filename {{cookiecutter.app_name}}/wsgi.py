# -*- coding: utf-8 -*-
"""
    wsgi.py
    ~~~~~~~

    Flask-Script Command to execute a set of Flask applications
    combined using DispatcherMiddleware.

    :author: {{ cookiecutter.author }}
    :copyright: © {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.

    templated from https://github.com/ryanolson/cookiecutter-webapp
"""
from flask.ext.script import Command
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from {{ cookiecutter.app_name }} import api
from {{ cookiecutter.app_name }} import frontend

application = DispatcherMiddleware(
    frontend.create_app(), {
#       '/api': api.create_app(),
    })

class Server(Command):
    """
    Run the Flask development server, aka run_simple from werkzeug.

    :param host: server host
    :param port: server port
    :param use_debugger: Flag whether to default to using the Werkzeug debugger.
                         This can be overriden in the command line
                         by passing the **-d** or **-D** flag.
                         Defaults to False for security.
    :param use_reloader: Flag whether to use the auto-reloader.
                         Default to True when debugging.
                         This can be overriden in the command line by
                         passing the **-r**/**-R** flag.
    :param threaded: should the process handle each request in a separate
                     thread? Defaults to False.
    :param processes: number of processes to spawn.  Defaults to 1.
    :param passthrough_errors: disable the error catching. This means that the
                               server will die on errors but it can be useful
                               to hook debuggers in (pdb etc.)
    :param options: :func:`werkzeug.run_simple` options.
    """
    help = description = 'Runs the Flask development server i.e. app.run()'

    def __init__(self, host='127.0.0.1', port=5000, use_debugger=None,
                 use_reloader=None, threaded=False, processes=1,
                 passthrough_errors=False, **options):

        self.port = port
        self.host = host
        self.use_debugger = use_debugger
        self.use_reloader = use_reloader if use_reloader is not None else use_debugger
        self.server_options = options
        self.threaded = threaded
        self.processes = processes
        self.passthrough_errors = passthrough_errors

    def get_options(self):

        options = (
            Option('-h', '--host',
                   dest='host',
                   default=self.host),

            Option('-p', '--port',
                   dest='port',
                   type=int,
                   default=self.port),

            Option('--threaded',
                   dest='threaded',
                   action='store_true',
                   default=self.threaded),

            Option('--processes',
                   dest='processes',
                   type=int,
                   default=self.processes),

            Option('--passthrough-errors',
                   action='store_true',
                   dest='passthrough_errors',
                   default=self.passthrough_errors),

            Option('-d', '--debug',
                   action='store_true',
                   dest='use_debugger',
                   help='enable the Werkzeug debugger (DO NOT use in production code)',
                   default=self.use_debugger),
            Option('-D', '--no-debug',
                   action='store_false',
                   dest='use_debugger',
                   help='disable the Werkzeug debugger',
                   default=self.use_debugger),

            Option('-r', '--reload',
                   action='store_true',
                   dest='use_reloader',
                   help='monitor Python files for changes (not 100% safe for production use)',
                   default=self.use_reloader),

            Option('-R', '--no-reload',
                   action='store_false',
                   dest='use_reloader',
                   help='do not monitor Python files for changes',
                   default=self.use_reloader),
            )

        return options

    def __call__(self, app, host, port, use_debugger, use_reloader,
               threaded, processes, passthrough_errors):
        # we don't need to run the server in request context
        # so just run it directly

        if use_debugger is None:
            use_debugger = app.debug

        if use_debugger is None:
            use_debugger = True
        #   if sys.stderr.isatty():
        #       print(("Debugging is on. DANGER: Do not allow random ",
        #              "users to connect to this server."), file=sys.stderr)

        if use_reloader is None:
            use_reloader = app.debug

        run_simple(host, port, application,
                debug=use_debugger,
                use_debugger=use_debugger,
                use_reloader=use_reloader,
                threaded=threaded,
                processes=processes,
                passthrough_errors=passthrough_errors,
                **self.server_options)

if __name__ == "__main__":
    server = Server(use_debugger=True, use_reloader=True)
    server()
    #run_simple('0.0.0.0', 5000, application, use_reloader=True, use_debugger=True)
