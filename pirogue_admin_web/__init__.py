
import multiprocessing

from flask import Flask
from gunicorn.app.wsgiapp import WSGIApplication
from gunicorn.util import import_app


class StandaloneApplication(WSGIApplication):
    def __init__(self, app_uri, options=None, flask_config=None):
        self.app_uri = app_uri
        self.options = options or {}
        self.flask_config = flask_config or {}
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        flask_app = import_app(self.app_uri)

        if isinstance(flask_app, Flask):
            for key, val in self.flask_config.items():
                flask_app.config[key] = val
                if key == 'STATIC_FOLDER':
                    flask_app.static_folder = val
        return flask_app

def serve(dev=False):
    options = {
        "bind": "0.0.0.0:4242" if dev else "localhost:4242",
        #"workers": (multiprocessing.cpu_count() * 2),
        #'worker_class': 'gunicorn.workers.gthread.ThreadWorker',
    }
    flask_config = {
        'APPLICATION_ROOT': '/' if dev else '/admin',
        'STATIC_FOLDER': '../dist' if dev else '/usr/share/pirogue-admin-web/htdocs',
    }

    StandaloneApplication("pirogue_admin_web.server:app", options, flask_config).run()


if __name__ == '__main__':
    serve(dev=True)