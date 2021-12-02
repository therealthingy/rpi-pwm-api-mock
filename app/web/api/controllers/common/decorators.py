from app.web.api.controllers.common.responses import new_bad_request_response, \
    new_internal_server_err_response, \
    new_not_supported_yet_feature_response

from app.core.utils.logger import generate_log_uuid


class SortArg:
    """
    Represents parsed sort string passed via API
    """
    def __init__(self, order, attr, clz_sortable_attrs):
        if not (order in ["+", "-"]): raise ValueError(f"Invalid order specifier (\"{order}\")")
        self._asc = order == "+"

        if not attr or not (attr in clz_sortable_attrs): raise ValueError(f"Unsortable attribute (\"{attr}\")")
        self._attr = attr

    def __repr__(self):
        return "%s('%s', '%s')" % (SortArg.__name__, "+" if self.asc else "-", self.attribute)

    def __eq__(self, other):
        return self.attribute == other.attribute

    def __hash__(self):                 # Required for duplicate check (using `set`)
        return hash(self.attribute)

    @property
    def asc(self):
        return self._asc

    @property
    def attribute(self):
        return self._attr

    @classmethod
    def from_str(cls, sort_str, clz_sortable_attrs):
        """
        Creates list of parsed `SortArg`s from string

        Assumed "encoding": <order><property1>[,<order><property2>,...] where
            - order may be '+' for asc or '-' for desc
        """
        sort_args = [cls(attr_str[0], attr_str[1:], clz_sortable_attrs) for attr_str in sort_str.split(",") if attr_str]
        if len(set(sort_args)) != len(sort_args): raise ValueError("Duplicate sorting attributes")
        return sort_args


def enable_sort_post_db_fetch(*, clz_sortable_args, default=None):
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
                               reverse= not sort_args[0].asc) if sort_args else result
            except KeyError as ex:
                log_uuid = generate_log_uuid()
                # TODO: LOG ERROR AS ERROR
                return new_internal_server_err_response(101, "Defined sortable attribute doesn't exist", log_uuid)

        return inner_wrapper
    return wrapper
