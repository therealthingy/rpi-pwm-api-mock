from connexion import request

from app.web.persistence.repos import FanCurveRepo, ConfigRepo

from app.web.logic.sysinfo import SysStatsMock as SysStats
from app.web.logic.history import AppHistoryMock as AppHistory

from app.web.api.schemas import FanCurveSchema, ConfigSchema, \
    SysStatsSystemInfoSchema, SysStatsOSProcessSchema, \
    AppLogEntrySchema, AppTempDCHistoryEntrySchema

from app.web.api.controllers.responses import not_found_response, \
    optimistic_locking_response, \
    unsupported_media_type_response, \
    del_used_fancurve_response, \
    new_bad_request_response

from app.web.api.controllers.utils import calc_etag

from operator import attrgetter


# -- Globals --
config_schema = ConfigSchema()
fan_curve_schema = FanCurveSchema()
fan_curve_list_schema = FanCurveSchema(many=True)
stats_os_system_info_schema = SysStatsSystemInfoSchema()
stats_os_process_schema = SysStatsOSProcessSchema()
stats_os_process_list_schema = SysStatsOSProcessSchema(many=True)
stats_log_entry_list_schema = AppLogEntrySchema(many=True)
stats_temp_dc_entry_list_schema = AppTempDCHistoryEntrySchema(many=True)

sys_stats = SysStats()
app_history = AppHistory()


# -- Handlers --
def app_config_get():
    """Returns current config flags

    Returns current config flags

    :rtype: AppConfig
    """
    current_config = ConfigRepo.fetch_config()
    return config_schema.dump(current_config), {'ETag': calc_etag(current_config)}


def app_config_put():
    """Updates config flags

    Updates config flags

    :rtype: AppConfig
    """
    if request.is_json:
        updated_config = config_schema.load(request.get_json(), transient=True)

        current_config = ConfigRepo.fetch_config()
        if calc_etag(current_config) != str(request.if_match)[1:-1]:
            return optimistic_locking_response

        try: ConfigRepo.update_config(updated_config)
        except ValueError as ex: return new_bad_request_response(str(ex))
        return config_schema.dump(updated_config)

    return unsupported_media_type_response     # Note: Actually already caught before (by flask)


def app_fan_curves_did_delete(did):
    """Deletes fan curve whose id correspond to specified \&quot;did\&quot;

    Deletes fan curve whose id correspond to specified &#x60;did&#x60;

    :param did: Id of the fan curve (generated, i.e., surrogate key)
    :type did: str

    :rtype: None
    """
    try: return None if FanCurveRepo.delete(did) else not_found_response
    except ValueError: return del_used_fancurve_response


def app_fan_curves_did_get(did):
    """Returns requested fan curve whose id corresponds to specified \&quot;did\&quot;

    Returns requested fan curve whose id corresponds to specified &#x60;did&#x60;

    :param did: Id of the fan curve (generated, i.e., surrogate key)
    :type did: str

    :rtype: AppFanCurve
    """
    found_fan_curve = FanCurveRepo.find_by_id(did)
    return (fan_curve_schema.dump(found_fan_curve), {'ETag': calc_etag(found_fan_curve)}) \
        if not (found_fan_curve is None) else not_found_response


def app_fan_curves_did_put(did):
    """Updates requested fan curve whose id corresponds to specified \&quot;did\&quot;

    Updates requested fan curve whose id corresponds to specified &#x60;did&#x60;

    :param did: Id of the fan curve (generated, i.e., surrogate key)
    :type did: str

    :rtype: AppFanCurve
    """
    if request.is_json:
        updated_fan_curve = fan_curve_schema.load(request.get_json(), transient=True)
        found_fan_curve_entity = FanCurveRepo.find_by_id(did)

        if found_fan_curve_entity is None:
            return not_found_response

        if calc_etag(found_fan_curve_entity) != str(request.if_match)[1:-1]:
            return optimistic_locking_response

        updated_fan_curve.did = did
        FanCurveRepo.update(updated_fan_curve)
        return fan_curve_schema.dump(updated_fan_curve)

    return unsupported_media_type_response     # Note: Actually already caught before (by flask)


def app_fan_curves_get(name=None):
    """Returns list of all available fan curves

    Returns list of all available fan curves

    :param name: Filter for fan curves whose name is similar to &#x60;name&#x60;
    :type name: str

    :rtype: List[AppFanCurve]
    """
    return fan_curve_list_schema.dump(FanCurveRepo.find_all(name))


def app_fan_curves_post():
    """Adds new fan curve

    Adds new fan curve

    :rtype: AppFanCurve
    """
    if request.is_json:
        new_fan_curve = fan_curve_schema.load(request.get_json(), transient=True)
        FanCurveRepo.create(new_fan_curve)
        return fan_curve_schema.dump(new_fan_curve)

    return unsupported_media_type_response     # Note: Actually already caught before (by flask)


def app_logs_get():
    """Returns list of all available fan curves

    Returns list of all available fan curves

    :rtype: List[AppLogEntry]
    """
    sorted_logs = sorted(app_history.get_logs(), key=attrgetter('date'), reverse=True)
    return stats_log_entry_list_schema.dump(sorted_logs)


def app_temp_dc_history_get():
    """Returns temperature- &amp; fan history over last 10 min.

    Returns temperature- &amp; fan history over last 10 min.

    :rtype: List[AppTempDCHistoryEntry]
    """
    return stats_temp_dc_entry_list_schema.dump(app_history.get_temp_dc_history())


def system_info_get():
    """Returns information about used system (SW &amp; HW)

    Returns information about used system (SW &amp; HW)

    :rtype: SystemInfo
    """
    return stats_os_system_info_schema.dump(sys_stats.get_system_info())


def system_top_ten_processes_get():
    """Returns list of top 10 processes using the most CPU time

    Returns list of top 10 processes using the most CPU time

    :rtype: List[SystemProcess]
    """
    return stats_os_process_list_schema.dump(sys_stats.get_system_processes()[:10])


def system_top_ten_processes_nr_get(nr):
    """Returns requested process whose current CPU utilization corresponds to specified nr in ranking

    Returns requested process whose current CPU utilization corresponds to specified &#x60;nr&#x60; in ranking

    :param nr: Corresponds to process w/ &#x60;nr&#x60; highest CPU utilization at current moment
    :type nr: int

    :rtype: SystemProcess
    """
    try:
        index_nr = nr - 1
        if index_nr < 0: raise IndexError("Negative indices are not allowed")
        return stats_os_process_schema.dump(sys_stats.get_system_processes()[index_nr])
    except IndexError:
        return new_bad_request_response("Invalid value for `nr`")
