from app.web.api.controllers.common.parsing import SortArg
from app.web.api.controllers.common.responses import new_bad_request_response, \
    new_internal_server_err_response, \
    new_not_supported_yet_feature_response

from app.core.utils.logger import generate_log_uuid


def enable_sort_post_db_fetch(*, clz_sortable_args, default=None):
    """
    Must be applied on api controller function which returns list of dicts (e.g., which uses marshmallow-schema `dump`)
    """
    def wrapper(fct):
        def inner_wrapper(sort=None, **kwargs):
            sort_args = None
            if sort:
                try: sort_args = SortArg.from_str(sort, clz_sortable_args)
                except ValueError as ex: return new_bad_request_response(str(ex))
            elif default:
                try: sort_args = SortArg.from_str(default, clz_sortable_args)
                except ValueError as ex:
                    log_uuid = generate_log_uuid()
                    # TODO: LOG ERROR AS ERROR
                    return new_internal_server_err_response(101, "Malformed default sort expression", log_uuid)

            if sort_args and len(sort_args) > 1:        # TODO: Add support for more than 1
                return new_not_supported_yet_feature_response("Sorting by more than one attribute")

            result = fct(**kwargs)
            try: return sorted(result, key=lambda d: d[sort_args[0].attribute],
                               reverse=not sort_args[0].asc) if sort_args else result
            except KeyError as ex:
                log_uuid = generate_log_uuid()
                # TODO: LOG ERROR AS ERROR
                return new_internal_server_err_response(101, "Defined sortable attribute doesn't exist", log_uuid)

        return inner_wrapper
    return wrapper
