from typing import List
from app.envflags import api_auth_user, api_auth_pass


def info_from_api_security(username, password, required_scopes):
    """
    Check and retrieve authentication information from basic auth.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.

    :param username login provided by Authorization header
    :type username: str
    :param password password provided by Authorization header
    :type password: str
    :param required_scopes Always None. Used for other authentication method
    :type required_scopes: None
    :return: Information attached to user or None if credentials are invalid or does not allow access to called API
    :rtype: dict | None
    """
    if username == api_auth_user and password == api_auth_pass:
        return {'sub': api_auth_user, 'scope': 'api-security'}
    else:
        return None
