'''
Backend which is run in an dedicated Thread
'''


def new_launchable_backend():
    # -- API config --
    from app.envflags import api_swagger_ui_enabled, api_server_port
    from connexion import App as ConnexionApp
    import app.api.encoder as encoder

    app = ConnexionApp(__name__, specification_dir='../api/openapi/',
                       options={"swagger_ui": api_swagger_ui_enabled})
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'rpi-pwm'},
                pythonic_params=True)

    # -- Logging config --
    # app.

    return lambda: app.run(port=api_server_port)


def launch_as_new_thread():
    import threading
    app_backend = new_launchable_backend()
    return lambda: threading.Thread(target=app_backend, daemon=True).start()        # Note: Deamon threads exit automatically as soon as main thread exits
