"""
Backend serving the API
    -> Must be run in separate thread
"""
from app.core.envflags import app_debug_mode, api_swagger_ui_enabled, api_server_port
from app.web.api.controllers.responses import semantic_validation_failed
from app.web.persistence.db import db

from connexion import App as ConnexionApp
from flask_marshmallow import Marshmallow
from marshmallow.exceptions import ValidationError


# -- Globals --
_DB_FILE_PATH = "/var/lib/rpi-pwm/config.db"        # Path in Docker container (should be a mapped Docker volume)

ma = Marshmallow()


def _new_connex_app():
    connex_app = ConnexionApp(__name__,
                              specification_dir='./api/',
                              options={"swagger_ui": api_swagger_ui_enabled})
    connex_app.add_api('openapi.yaml',
                       arguments={'title': 'rpi-pwm'},
                       pythonic_params=True)

    return connex_app


def _init_db(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    if app_debug_mode:
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
        app.config['SQLALCHEMY_ECHO'] = True
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + _DB_FILE_PATH


    with app.app_context():
        db.init_app(app)
        db.create_all()


def _init_marshmallow(app):
    with app.app_context():
        ma.init_app(app)

    @app.errorhandler(ValidationError)
    def register_validation_error(error):           # Would be otherwise a 500
        return semantic_validation_failed


# -- Functions --
def new_runnable_backend():
    connex_app = _new_connex_app()

    _init_db(connex_app.app)
    _init_marshmallow(connex_app.app)

    # TODO: Logging

    return lambda: connex_app.run(port=api_server_port)


def launch_as_new_thread():
    import threading
    app_backend = new_runnable_backend()
    return lambda: threading.Thread(target=app_backend, daemon=True).start()        # Note: Deamon threads exit automatically as soon as main thread exits
