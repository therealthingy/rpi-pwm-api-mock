'''
Functions pertinent for API authentication
'''

import os
from app import defaults


_username = (os.getenv('API_AUTH_USER') or defaults.DEFAULT_API_AUTH_USER)
_password = (os.getenv('API_AUTH_PASS') or defaults.DEFAULT_API_AUTH_PASS)

def basic_auth(username, password, required_scopes=None):
    if username == _username and password == _password:
        return {'sub': 'admin', 'scope': 'api-security'}
    else:
        return None