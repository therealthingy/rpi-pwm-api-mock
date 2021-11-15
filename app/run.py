#!/usr/bin/env python3

from connexion import App as ConnexionApp, RestyResolver as ConnexionRestyResolver
import os
# import app
from defaults import DEFAULT_API_SERVER_PORT


if __name__ == '__main__':
    app = ConnexionApp(__name__, specification_dir='api/')
    app.add_api('specification.yaml', resolver=ConnexionRestyResolver('api.handlers'), resolver_error=501)
    app.run(port=int(os.getenv('API_SERVER_PORT') or DEFAULT_API_SERVER_PORT))
