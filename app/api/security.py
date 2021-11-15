"""
API authentication

# TODO: ADD       x-basicInfoFunc: api.security.basic_auth2
Example: https://github.com/zalando/connexion/tree/main/examples/openapi3/basicauth

Documentation: https://connexion.readthedocs.io/en/latest/security.html
"""

import os
from app import defaults


_username = (os.getenv('API_AUTH_USER') or defaults.DEFAULT_API_AUTH_USER)
_password = (os.getenv('API_AUTH_PASS') or defaults.DEFAULT_API_AUTH_PASS)

def basic_auth(username, password, required_scopes=None):
    if username == _username and password == _password:
        return {'sub': 'admin', 'scope': 'secret'}
    else:
        # optional: raise exception for custom error response
        return None