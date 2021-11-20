import app.web.api.models
import connexion
import six

from app.web.api.models.app_config import AppConfig  # noqa: E501
from app.web.api.models.app_fan_curve import AppFanCurve  # noqa: E501
from app.web.api.models.app_fan_curve_base import AppFanCurveBase  # noqa: E501
from app.web.api.models.app_log_entry import AppLogEntry  # noqa: E501
from app.web.api.models.app_temp_dc_history_entry import AppTempDCHistoryEntry  # noqa: E501
from app.web.api.models.system_info import SystemInfo  # noqa: E501
from app.web.api.models.system_process import SystemProcess  # noqa: E501
from app.web.api import util

from app.web.api.models.http_error import HTTPError
from app.web.persistence.repositories import FanCurveRepo, ConfigRepo
from app.web.api.types_mapper import entity_to_model, model_to_entity

import flask


# -- Errors + Responses --
_unsupported_media_type_error = HTTPError(415, "Unsupported Media Type", 0, "API Error", None)     # Note: Already handeled by Flask (only for code completion)
_unsupported_media_type_response = (_unsupported_media_type_error, _unsupported_media_type_error.http_status_code)
_locked_resource_error = HTTPError(423, "Locked", 0, "API Error - Requested resource cannot be deleted b/c its currently used", None)
_locked_resource_response = (_locked_resource_error, _locked_resource_error.http_status_code)
_not_found_error = HTTPError(404, "Not Found", 0, "API Error", None)
_not_found_response = (_not_found_error, _not_found_error.http_status_code)
_not_implemented_yet_error = HTTPError(501, "Not Implemented", 0, "API Error - Functionality accessible via API isn't implemented yet", None)
_not_implemented_yet_response = (_not_implemented_yet_error, _not_implemented_yet_error.http_status_code)


# !! TODO: ADD ETAG EVERYWHERE !!


# -- Handlers --
def app_config_get():  # noqa: E501
    """Returns current config flags

    Returns current config flags # noqa: E501


    :rtype: AppConfig
    """
    return entity_to_model(ConfigRepo.fetch_config())


def app_config_put(body):  # noqa: E501     # $$ OG: if_match, app_config $$
    """Updates config flags

    Updates config flags # noqa: E501

    :param if_match: Current hash of to be updated config -&gt; used for optimistic locking
    :type if_match: str
    :param app_config: Config flags consisting of app and pwm config
    :type app_config: dict | bytes

    :rtype: AppConfig
    """
    if connexion.request.is_json:
        # TODO: CHECK If-Match; Locking ?
        print(connexion.request.if_match)

        app_config = AppConfig.from_dict(connexion.request.get_json())  # noqa: E501

        new_app_config = model_to_entity(app_config)
        try: ConfigRepo.update_config(new_app_config)
        except ValueError: return HTTPError(400, "Bad request", 0, "API Error - Selected fan curve doesn't exist", None), 400

        return entity_to_model(new_app_config)                                  # Note: `entity_to_model` defaults to 200

    return _unsupported_media_type_response


def app_fan_curves_did_delete(did):  # noqa: E501
    """Deletes fan curve whose id correspond to specified \&quot;did\&quot;

    Deletes fan curve whose id correspond to specified &#x60;did&#x60; # noqa: E501

    :param did: Id of the fan curve (generated, i.e., surrogate key)
    :type did: str

    :rtype: None
    """
    try:
        return None if FanCurveRepo.delete(did) else _not_found_response        # Note: `None` defaults to 204
    except ValueError:
        return _locked_resource_response


def app_fan_curves_did_get(did):  # noqa: E501
    """Returns requested fan curve whose id corresponds to specified \&quot;did\&quot;

    Returns requested fan curve whose id corresponds to specified &#x60;did&#x60; # noqa: E501

    :param did: Id of the fan curve (generated, i.e., surrogate key)
    :type did: str

    :rtype: AppFanCurve
    """
    found_fan_curve = FanCurveRepo.find_by_id(did)
    return entity_to_model(found_fan_curve) if found_fan_curve is not None \
        else (_not_found_error, _not_found_error.http_status_code)              # Note: `entity_to_model` defaults to 200


def app_fan_curves_did_put(did, body):  # noqa: E501        # $$ OG: `did, if_match, app_fan_curve_base` $$
    """Updates requested fan curve whose id corresponds to specified \&quot;did\&quot;

    Updates requested fan curve whose id corresponds to specified &#x60;did&#x60; # noqa: E501

    :param did: Id of the fan curve (generated, i.e., surrogate key)
    :type did: str
    :param if_match: Current hash of to be updated fan curve -&gt; used for optimistic locking
    :type if_match: str
    :param app_fan_curve_base: Must contain the the updated fan curve corresponding to &#x60;did&#x60;
    :type app_fan_curve_base: dict | bytes

    :rtype: AppFanCurve
    """
    # TODO: CHECK If-Match
    print(connexion.request.if_match)

    if connexion.request.is_json:
        app_fan_curve_base = AppFanCurveBase.from_dict(connexion.request.get_json())  # noqa: E501
        found_fan_curve_entity = FanCurveRepo.find_by_id(did)
        if found_fan_curve_entity is not None:
            updated_fan_curve_entity = model_to_entity(app_fan_curve_base)
            updated_fan_curve_entity.did = did
            FanCurveRepo.update(updated_fan_curve_entity)
            return entity_to_model(updated_fan_curve_entity)                    # Note: `entity_to_model` defaults to 200
        return _not_found_response

    return _unsupported_media_type_response


def app_fan_curves_get(name=None):  # noqa: E501
    """Returns list of all available fan curves

    Returns list of all available fan curves # noqa: E501

    :param name: Filter for fan curves whose name is similar to &#x60;name&#x60;
    :type name: str

    :rtype: List[AppFanCurve]
    """
    return [entity_to_model(x) for x in FanCurveRepo.find_all(name)]


def app_fan_curves_post(body):  # noqa: E501        # $$ OG: `app_fan_curve_base, name=None` $$
    """Adds new fan curve

    Adds new fan curve # noqa: E501

    :param app_fan_curve_base: 
    :type app_fan_curve_base: dict | bytes
    :param name: Filter for fan curves whose name is similar to &#x60;name&#x60;
    :type name: str

    :rtype: AppFanCurve
    """
    if connexion.request.is_json:
        app_fan_curve = AppFanCurveBase.from_dict(connexion.request.get_json())  # noqa: E501
        new_fancurve = model_to_entity(app_fan_curve)
        FanCurveRepo.create(new_fancurve)
        return entity_to_model(new_fancurve)

    return _unsupported_media_type_response


def app_logs_get():  # noqa: E501
    """Returns list of all available fan curves

    Returns list of all available fan curves # noqa: E501


    :rtype: List[AppLogEntry]
    """
    return _not_implemented_yet_response           # TODO


def app_temp_dc_history_get():  # noqa: E501
    """Returns temperature- &amp; fan history over last 10 min.

    Returns temperature- &amp; fan history over last 10 min. # noqa: E501


    :rtype: List[AppTempDCHistoryEntry]
    """
    return _not_implemented_yet_response           # TODO


def system_info_get():  # noqa: E501
    """Returns information about used system (SW &amp; HW)

    Returns information about used system (SW &amp; HW) # noqa: E501


    :rtype: SystemInfo
    """
    return _not_implemented_yet_response           # TODO


def system_top_ten_processes_get():  # noqa: E501
    """Returns list of top 10 processes using the most CPU time

    Returns list of top 10 processes using the most CPU time # noqa: E501


    :rtype: List[SystemProcess]
    """
    return _not_implemented_yet_response           # TODO


def system_top_ten_processes_nr_get(nr):  # noqa: E501
    """Returns requested process whose current CPU utilization corresponds to specified nr in ranking

    Returns requested process whose current CPU utilization corresponds to specified &#x60;nr&#x60; in ranking # noqa: E501

    :param nr: Corresponds to process w/ &#x60;nr&#x60; highest CPU utilization at current moment
    :type nr: int

    :rtype: SystemProcess
    """
    return _not_implemented_yet_response           # TODO
