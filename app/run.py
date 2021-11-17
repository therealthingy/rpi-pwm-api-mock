#!/usr/bin/env python3

import os
from distutils.util import strtobool
from defaults import DEFAULT_API_SERVER_PORT, DEFAULT_API_ENABLED, DEFAULT_API_SWAGGER_UI_ENABLED
# import app


api_enabled = strtobool(os.getenv('API_ENABLED', str(DEFAULT_API_ENABLED)))
api_server_port = int(os.getenv('API_SERVER_PORT', DEFAULT_API_SERVER_PORT))
api_swagger_ui_enabled = strtobool(os.getenv('API_SWAGGER_UI_ENABLED', str(DEFAULT_API_SWAGGER_UI_ENABLED)))


if __name__ == '__main__':
    # - PWM (controls fan) -
    ...

    # - API -
    if api_enabled:
        # TODO: Log "starting API"
        from connexion import App as ConnexionApp, RestyResolver as ConnexionRestyResolver
        app = ConnexionApp(__name__, specification_dir='api/', options={"swagger_ui": api_swagger_ui_enabled})
        app.add_api('specification.yaml', resolver=ConnexionRestyResolver('api.handlers'), resolver_error=501)
        app.run(port=api_server_port)

