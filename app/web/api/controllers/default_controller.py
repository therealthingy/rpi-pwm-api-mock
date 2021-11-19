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

from app.web.persistence.repositories import FanCurveRepo, ConfigRepo
from app.web.api.types_mapper import entity_to_model, model_to_entity


# -- Functions --
def app_config_get():  # noqa: E501
    """Returns current config flags

    Returns current config flags # noqa: E501


    :rtype: AppConfig
    """
    # TODO: ADD ETAG

    config = ConfigRepo.fetch_config()
    return entity_to_model(config), 200


def app_config_put(body):  # noqa: E501       # $$ OG: `if_match, app_config` $$
    """Updates config flags

    Updates config flags # noqa: E501

    :param if_match: Current hash of to be updated config -&gt; used for optimistic locking
    :type if_match: str
    :param app_config: Config flags consisting of app and pwm config
    :type app_config: dict | bytes

    :rtype: AppConfig
    """
    if connexion.request.is_json:
        # TODO: CHECK If-Match
        app_config = AppConfig.from_dict(connexion.request.get_json())  # noqa: E501

        # FanCurveRepo.fetch_by_id(app_config.selected_fan_curve._id)

        ConfigRepo.update_config(model_to_entity(app_config))
        return app_config, 200

    return {"error": "Unsupported Media Type"}, 415    #  TODO: ??


def app_fan_curves_get(name=None):  # noqa: E501
    """Returns list of all available fan curves

    Returns list of all available fan curves # noqa: E501

    :param name: Filter for fan curves whose name is similar to &#x60;name&#x60;
    :type name: str

    :rtype: List[AppFanCurve]
    """
    return FanCurveRepo.fetch_all()


def app_fan_curves_id_delete(id_):  # noqa: E501       # $$ OG: `id` $$
    """Deletes fan curve whose id correspond to specified \&quot;id\&quot;

    Deletes fan curve whose id correspond to specified &#x60;id&#x60; # noqa: E501

    :param id: Id of the fan curve (generated, i.e., surrogate key)
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def app_fan_curves_id_get(id_):  # noqa: E501       # $$ OG: `id` $$
    """Returns requested fan curve whose id corresponds to specified \&quot;id\&quot;

    Returns requested fan curve whose id corresponds to specified &#x60;id&#x60; # noqa: E501

    :param id: Id of the fan curve (generated, i.e., surrogate key)
    :type id: str

    :rtype: AppFanCurve
    """
    return 'do some magic!'


def app_fan_curves_id_put(id_, body):  # noqa: E501       # $$ OG: `id, if_match, app_fan_curve_base` $$
    """Updates requested fan curve whose id corresponds to specified \&quot;id\&quot;

    Updates requested fan curve whose id corresponds to specified &#x60;id&#x60; # noqa: E501

    :param id: Id of the fan curve (generated, i.e., surrogate key)
    :type id: str
    :param if_match: Current hash of to be updated fan curve -&gt; used for optimistic locking
    :type if_match: str
    :param app_fan_curve_base: Must contain the the updated fan curve corresponding to &#x60;id&#x60;
    :type app_fan_curve_base: dict | bytes

    :rtype: AppFanCurve
    """
    if connexion.request.is_json:
        app_fan_curve_base = AppFanCurveBase.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def app_fan_curves_post(body):  # noqa: E501       # $$ OG: `app_fan_curve_base, name=None` $$
    """Adds new fan curve

    Adds new fan curve # noqa: E501

    :param app_fan_curve_base: 
    :type app_fan_curve_base: dict | bytes
    :param name: Filter for fan curves whose name is similar to &#x60;name&#x60;
    :type name: str

    :rtype: AppFanCurve
    """
    if connexion.request.is_json:
        app_fan_curve_base = AppFanCurveBase.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def app_logs_get():  # noqa: E501
    """Returns list of all available fan curves

    Returns list of all available fan curves # noqa: E501


    :rtype: List[AppLogEntry]
    """
    return 'do some magic!'


def app_temp_dc_history_get():  # noqa: E501
    """Returns temperature- &amp; fan history over last 10 min.

    Returns temperature- &amp; fan history over last 10 min. # noqa: E501


    :rtype: List[AppTempDCHistoryEntry]
    """
    return 'do some magic!'


def system_info_get():  # noqa: E501
    """Returns information about used system (SW &amp; HW)

    Returns information about used system (SW &amp; HW) # noqa: E501


    :rtype: SystemInfo
    """
    return 'do some magic!'


def system_top_ten_processes_get():  # noqa: E501
    """Returns list of top 10 processes using the most CPU time

    Returns list of top 10 processes using the most CPU time # noqa: E501


    :rtype: List[SystemProcess]
    """
    return 'do some magic!'


def system_top_ten_processes_nr_get(nr):  # noqa: E501
    """Returns requested process whose current CPU utilization corresponds to specified nr in ranking

    Returns requested process whose current CPU utilization corresponds to specified &#x60;nr&#x60; in ranking # noqa: E501

    :param nr: Corresponds to process w/ &#x60;nr&#x60; highest CPU utilization at current moment
    :type nr: int

    :rtype: SystemProcess
    """
    return 'do some magic!'
