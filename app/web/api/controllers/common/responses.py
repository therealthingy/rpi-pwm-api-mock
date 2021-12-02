"""
Collection of standard HTTP responses (used across controllers)

Note: `appErrorCode`: are consecutively numbered for backend (500 type) errors, client errors are always 0
            -> Mock currently does NOT have any (intentional) 500 type errors
"""
from app.web.api.models import HTTPError


# -- Flask controller responses --
new_bad_request_response = lambda error_msg: (
        HTTPError(400, f"Bad Request ({error_msg})", 0, "N/A (Client error)"), 400)

_not_found_error = HTTPError(404, "Not Found (Requested resource couldn't be found)", 0, "N/A (Client error)")
not_found_response = (_not_found_error, _not_found_error.http_status_code)

_optimistic_locking_error = HTTPError(409, "Conflict (Optimistic locking violation: Requested resource has "
                                           "been updated in the meantime)", 0, "N/A (Client error)")
optimistic_locking_response = (_optimistic_locking_error, _optimistic_locking_error.http_status_code)

_del_used_fancurve_error = HTTPError(423, "Locked (Requested fan curve cannot be deleted b/c it's "
                                          "currently used)", 0, "N/A (Client error)")
del_used_fancurve_response = (_del_used_fancurve_error, _del_used_fancurve_error.http_status_code)

# - Already handled by Flask (only for code completion) -
_unsupported_media_type_error = HTTPError(415, "Unsupported Media Type", 0, "N/A (Client error)")
unsupported_media_type_response = (_unsupported_media_type_error, _unsupported_media_type_error.http_status_code)

new_not_supported_yet_feature_response = lambda feature: (
        HTTPError(501, "Not Implemented", 0, f"{feature} is not (yet) supported"), 501)


# -- Flask registered error handler responses --
new_semantic_validation_failed_response = lambda error_msg="semantic error": (
        HTTPError(422, f"Unprocessable Entity ({error_msg})", 0, "N/A (Client error)"), 422)
