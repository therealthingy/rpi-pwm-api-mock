"""
Collection of standard HTTP responses (used across controllers)
"""
from app.web.api.models import HTTPError


_not_found_error = HTTPError(404, "Not Found", 0, "API Error", None)
not_found = (_not_found_error, _not_found_error.http_status_code)

_optimistic_locking_error = HTTPError(409, "Conflict", 0, "API Error - Requested resource has been most likely updated in the meantime", None)
optimistic_locking = (_optimistic_locking_error, _optimistic_locking_error.http_status_code)

_unsupported_media_type_error = HTTPError(415, "Unsupported Media Type", 0, "API Error", None)     # Note: Already handeled by Flask (only for code completion)
unsupported_media_type = (_unsupported_media_type_error, _unsupported_media_type_error.http_status_code)

_locked_resource_error = HTTPError(423, "Locked", 0, "API Error - Requested resource cannot be deleted b/c its currently used", None)
locked_resource = (_locked_resource_error, _locked_resource_error.http_status_code)

_semantic_error = HTTPError(422, "Unprocessable Entity", 0, "API Error - Sent entity is semantically incorrect", None)
semantic_validation_failed = (_semantic_error, _semantic_error.http_status_code)