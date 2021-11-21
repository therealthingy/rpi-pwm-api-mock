"""
Backend serving the API
    -> Must be run in separate thread
"""
from app.core.envflags import api_swagger_ui_enabled, api_server_port
from connexion import App as ConnexionApp
from app.web.persistence.db import db

from flask_marshmallow import Marshmallow


# -- Glboals --
_DB_FILE_PATH = "/tmp/rpi-pwm.db"

ma = Marshmallow()


# -- Functions --
def new_launchable_backend():
    # -- API config --
    connex_app = ConnexionApp(__name__,
                              specification_dir='./api/',
                              options={"swagger_ui": api_swagger_ui_enabled})
    connex_app.add_api('openapi.yaml',
                       arguments={'title': 'rpi-pwm'},
                       pythonic_params=True)

    # -- Logging config --
    # app.

    # -- Setup app (mainly db config) --
    connex_app.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + _DB_FILE_PATH
    connex_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    connex_app.app.config['PROPAGATE_EXCEPTIONS'] = True

    with connex_app.app.app_context():
        db.init_app(connex_app.app)
        db.create_all()
        ma.init_app(connex_app.app)

    return lambda: connex_app.run(port=api_server_port)


def launch_as_new_thread():
    import threading
    app_backend = new_launchable_backend()
    return lambda: threading.Thread(target=app_backend, daemon=True).start()        # Note: Deamon threads exit automatically as soon as main thread exits
