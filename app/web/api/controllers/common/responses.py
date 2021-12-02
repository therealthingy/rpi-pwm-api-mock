"""
Collection of standard HTTP responses (used across controllers)

Note: `appErrorCode`: are consecutively numbered for backend (500 type) errors,
            - client errors are always 0
            - server errors:
                - 1xx = API errors (e.g., parsing of args)
                - 2xx = PWM errors
                - 3xx = Misc.
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

new_exists_already_response = lambda error_msg: (
        HTTPError(409, f"Conflict ({error_msg})", 0, "N/A (Client error)"), 409)

_del_used_fancurve_error = HTTPError(423, "Locked (Requested fan curve cannot be deleted b/c it's "
                                          "currently used)", 0, "N/A (Client error)")
del_used_fancurve_response = (_del_used_fancurve_error, _del_used_fancurve_error.http_status_code)

new_internal_server_err_response = lambda app_err_num, app_err_msg, log_uuid: (
    HTTPError(500, "Internal Server Error", app_err_num, app_err_msg, log_uuid), 500)

new_not_supported_yet_feature_response = lambda feature: (
        HTTPError(501, "Not Implemented", 100, f"{feature} is not (yet) supported"), 501)


# -- Flask registered error handler responses --
new_semantic_validation_failed_response = lambda error_msg="semantic error": (
        HTTPError(422, f"Unprocessable Entity ({error_msg})", 0, "N/A (Client error)"), 422)
