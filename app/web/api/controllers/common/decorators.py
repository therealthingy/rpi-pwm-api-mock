from app.web.api.controllers.common.parsing import SortArg
from operator import attrgetter
from app.web.api.controllers.common.responses import new_bad_request_response, \
    new_not_supported_yet_feature_response


def enable_sort_post_db_fetch(*, clz_sortable_args):
    def wrapper(fct):
        def inner_wrapper(sort, *pargs, **kwargs):
            sort_args = None
            if sort:
                try: sort_args = SortArg.from_str(sort, clz_sortable_args)
                except ValueError as ex: return new_bad_request_response(str(ex))

            if sort_args and len(sort_args) > 1:
                return new_not_supported_yet_feature_response("Sorting by more than one attribute")

            result = fct(sort, *pargs, **kwargs)
            # TODO: TRY
            return sorted(result, key=attrgetter('adsf'), reverse=True) if sort_args else result

        return inner_wrapper
    return wrapper
