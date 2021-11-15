#!/usr/bin/env python3

import connexion
import os
# import app


_DEFAULT_PORT = 8080


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='api/')
    app.add_api('specification.yaml', resolver_error=501)
    app.run(port=int(os.getenv('API_SERVER_PORT') or _DEFAULT_PORT))
