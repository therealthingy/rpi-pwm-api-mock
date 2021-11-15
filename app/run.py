#!/usr/bin/env python3

import os
from defaults import DEFAULT_API_SERVER_PORT, DEFAULT_API_ENABLED
# import app


api_enabled = os.getenv('API_ENABLED') == 'True' or DEFAULT_API_ENABLED

if __name__ == '__main__':
    if api_enabled:
        # TODO: Log starting API
        from connexion import App as ConnexionApp, RestyResolver as ConnexionRestyResolver
        webapi = ConnexionApp(__name__, specification_dir='api/')
        webapi.add_api('specification.yaml', resolver=ConnexionRestyResolver('api.handlers'), resolver_error=501)
        webapi.run(port=int(os.getenv('API_SERVER_PORT') or DEFAULT_API_SERVER_PORT))
