#!/usr/bin/env python3

from app.envflags import api_enabled, api_swagger_ui_enabled, api_server_port
# import app




if __name__ == '__main__':
    # - PWM (controls fan) -
    ...

    # - API -
    if api_enabled:
        # TODO: Log "starting API"
        from connexion import App as ConnexionApp
        import api.encoder as encoder

        app = ConnexionApp(__name__, specification_dir='./api/openapi/',
                           options={"swagger_ui": api_swagger_ui_enabled})
        app.app.json_encoder = encoder.JSONEncoder
        app.add_api('openapi.yaml',
                    arguments={'title': 'rpi-pwm'},
                    pythonic_params=True)
        app.run(port=api_server_port)
