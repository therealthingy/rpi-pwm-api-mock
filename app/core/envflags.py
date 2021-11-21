'''
Contains flags which are set (and can only be set) via environment variables
'''
import os
from distutils.util import strtobool


# -- Default config flags (may be overwritten via environment variable) --
DEFAULT_API_ENABLED = True
DEFAULT_API_SERVER_PORT = 8080
DEFAULT_API_SWAGGER_UI_ENABLED = True

DEFAULT_API_AUTH_USER = "admin"
DEFAULT_API_AUTH_PASS = "admin"


api_enabled = strtobool(os.getenv('API_ENABLED', str(DEFAULT_API_ENABLED)))
api_server_port = int(os.getenv('API_SERVER_PORT', DEFAULT_API_SERVER_PORT))
api_swagger_ui_enabled = strtobool(os.getenv('API_SWAGGER_UI_ENABLED', str(DEFAULT_API_SWAGGER_UI_ENABLED)))

api_auth_user = os.getenv('API_AUTH_USER', DEFAULT_API_AUTH_USER)
api_auth_pass = os.getenv('API_AUTH_PASS', DEFAULT_API_AUTH_PASS)

# TODO: Add disable `system` endpoint flag (after presentation of mock)


# TODO: Use logger (instead of print) ...
print(f"Derived settings from env-vars.: {api_enabled=}, {api_server_port=}, {api_swagger_ui_enabled=}, {api_auth_user=}, {api_auth_pass=}")